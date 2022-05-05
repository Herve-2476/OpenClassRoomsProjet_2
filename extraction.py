#!usr/bin/env python
import requests
from bs4 import BeautifulSoup
import re

domaine = "http://books.toscrape.com"
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
r = requests.get(url).content
soup = BeautifulSoup(r,"html.parser")

#product_page_url
data = {}
data ["product_page_url"]=url

#universal_ product_code,price_excluding_tax,price_including_tax,number_available"
entrees={
        "UPC":"universal_ product_code",
        "Price (excl. tax)":"price_excluding_tax",
        "Price (incl. tax)":"price_including_tax",
        "Availability":"number_available",
        }
for e in soup.table.find_all("tr"):
    if e.th.string in entrees:
        data [entrees[e.th.string]]=e.td.string
data["number_available"] = int(re.findall(r'[\d]+', data["number_available"])[0])       

#product_description
e=soup.find_all("meta",{"name":"description"})[0]
data["product_description"] = e.attrs["content"].strip()

#category,title
e=soup.find_all("ul",class_="breadcrumb") [0]   
l_e=e.find_all("li")
data["category"] = l_e[2].a.string
data["title"] = l_e[3].string

#review_rating
for e in soup.find_all("p"):
    if "class" in e.attrs and e["class"][0]=="star-rating":
        data["review_rating"] = e["class"][1]

#image_url
data["image_url"] = domaine+soup.find_all("img")[0]["src"][5:]


for k in data:
    print (k,data[k])