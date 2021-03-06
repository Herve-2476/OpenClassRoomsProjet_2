import requests
from bs4 import BeautifulSoup
import re
import os
import csv

DOMAINE = "http://books.toscrape.com/"
REP_CSV="csv/"

def extraction_data_book(url):

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
    data["image_url"] = DOMAINE+soup.find_all("img")[0]["src"][6:]

    return data


def extraction_list_books_in_category(url):
    numero_page = 2
    list_book=[]
    while True:
        r = requests.get(url).content
        soup = BeautifulSoup(r,"html.parser")        
        for e in soup.find_all("h3"):
            list_book.append(DOMAINE+"catalogue"+e.a["href"][8:])

        if len(soup.find_all("li",class_="next"))==0:
            break
        url=os.path.dirname(url)+"/"+f"page-{numero_page}.html"
        numero_page+= 1

    return list_book

def creation_csv_by_category(url):
    l=extraction_list_books_in_category(url)
    data_books_in_category=[]
    for url_book in l:
        data_books_in_category.append(extraction_data_book(url_book))
    category=url.split("/")[-2].split("_")[0]
    with open(f"{REP_CSV}{category}.csv","w",encoding='utf-8') as f:
        obj = csv.DictWriter(f,data_books_in_category[0].keys())
        obj.writeheader()
        obj.writerows(data_books_in_category)
    print (f"Cat??gorie {category} trait??e ({len(l)} livres).")

url =   "http://books.toscrape.com/index.html"      
r = requests.get(url).content
soup = BeautifulSoup(r,"html.parser")

#cr??ation du r??pertoire csv si inexistant
os.makedirs(os.sep.join([os.getcwd(),REP_CSV]),exist_ok=True)

#r??cup??ration des cat??gories, des livres de chaque cat??gories et ??criture des fichiers csv
#un fichier csv par cat??gorie avec les donn??es indivuelles de chaque livre de cette cat??gories

for e in soup.find_all("ul",class_="nav nav-list")[0].li.ul.find_all("li"):
    url_category = DOMAINE+e.a["href"]    
    creation_csv_by_category(url_category)
    #break
    
