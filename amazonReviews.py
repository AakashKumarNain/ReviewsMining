import requests
from bs4 import BeautifulSoup

product_name=input("Enter a product name : ")

url = "http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + product_name
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

pid = soup.find_all("li",{"class":"s-result-item celwidget"})[0].get("data-asin")
plink = soup.find_all("li",{"class":"s-result-item celwidget"})[0].find_all("a",{"class":"a-link-normal s-access-detail-page  a-text-normal"})[0].get("href")

new_url = "http://www.amazon.in/product-reviews/" + pid + "/ref=acr_search_see_all?ie=UTF8&showViewpoints=1"
r = requests.get(new_url)
soup = BeautifulSoup(r.content,"html.parser")

print(soup.prettify())
