#!usr/bin/env python
import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
r = requests.get(url).content
soup = BeautifulSoup(r,"html.parser")

#print (soup.prettify())

#"UPC","Price (excl. tax)","Price (incl. tax)","Availability"
l_entrees=["UPC","Price (excl. tax)","Price (incl. tax)","Availability"]
for e in soup.table.find_all("tr"):
    if e.th.string in l_entrees:
        print (e.th.string+" = "+e.td.string)
        print()

e=soup.find_all("meta",{"name":"description"})[0] 

#product_page_url
print (url)
print()

#product_description
print (e.attrs["content"].strip())
print()
e=soup.find_all("ul",class_="breadcrumb") [0]   
l_e=e.find_all("li")

#category
print (l_e[2].a.string)
print()
#title
print (l_e[3].string)
print()
#review_rating
for e in soup.find_all("p"):
    if "class" in e.attrs and e["class"][0]=="star-rating":
        print (e["class"][1])
        print()

#image_url
print (soup.find_all("img")[0]["src"])
print()

