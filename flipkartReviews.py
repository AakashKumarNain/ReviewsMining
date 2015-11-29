import requests
from bs4 import BeautifulSoup

product_name = input("Enter a product name : ")
product_name = product_name.replace(" ","+")

url = "http://www.flipkart.com/search?q=" + product_name
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

pid = soup.find_all("div",{"class":"product-unit unit-4 browse-product new-design "})[0].get("data-pid")
plink = soup.find_all("div",{"class":"product-unit unit-4 browse-product new-design "})[0].find_all("a",{"class":"fk-display-block"})[0].get("href")

r = requests.get("http://www.flipkart.com"+plink)
soup = BeautifulSoup(r.content,"html.parser")

reviews_link = soup.find_all("a",{"class":"lnkViewAll"})[0].get("href")
reviews_link = "http://www.flipkart.com" + reviews_link.replace("sort=most_recent","type=top")

r = requests.get(reviews_link)
soup = BeautifulSoup(r.content,"html.parser")

##reviews = soup.find_all("div",{"class":"fclear fk-review fk-position-relative line "}).find_all("span",{"class":"review-text"})
##print(reviews)

reviews = soup.find_all("span",{"class":"review-text"})
for review in reviews:
    try:
        print(review.text,end="[END]")
        print("\n")
    except:
        pass
