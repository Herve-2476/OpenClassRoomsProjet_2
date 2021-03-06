import os
import csv
import requests

dir_csv = "csv"
dir_images = "images"
os.makedirs(dir_images,exist_ok=True)

liste_fichiers_csv=os.listdir(dir_csv)

for f in liste_fichiers_csv:
    n=0
    with open(os.sep.join([dir_csv,f]),"r",encoding='utf-8') as file:
        obj = csv.DictReader(file)
        for e in obj:
            image_url=e["image_url"]
            image_name = image_url.split("/")[-1]
            r = requests.get(image_url).content
            with open(os.sep.join([dir_images,image_name]),"wb") as im:
                im.write(r)
                n+= 1
    

    print (f"{n} images chargées dans la catégorie {f[:-4]}")           
            


