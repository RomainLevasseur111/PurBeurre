import requests
import mysql.connector
import json
from constants import *
from testclass import *

def requestprod():
    i = 1
    link = "https://fr.openfoodfacts.org/categorie/aliments-et-boissons-a-base-de-vegetaux"
    urls = []
    while i < NB_PAGEPRODUCT + 1:
        urls.append(link+"/"+str(i))
        i += 1

    print(urls)
    for l in urls :
        response = requests.request("GET", l+".json")
        json_prod = response.json()
        products_prod = json_prod.get('products')
        prod_code = [(data.get('id'), data.get('product_name'), data.get('generic_name'), data.get('url'), data.get('stores'), data.get('nutriscore_grade')) for data in products_prod]
        for prod in prod_code:
            product = Product(prod[0],prod[1],prod[2],prod[3],prod[4],prod[5])
            product.save()
            print(prod[1], " a été enregistré avec succés!")

def requestcat():

    response = requests.request("GET", cat_link)
    json_cat = response.json()
    tags_cat = json_cat.get('tags')[:NB_CATEGORY]
    name_cat = [(data.get('name'),) for data in tags_cat]
    link_cat = [(data.get('url'),) for data in tags_cat]
    for link in link_cat :
        print(link[0])
        #requestprod(link[0])
    for cat in name_cat:
        category = Categories(cat[0])
        category.saveCat()
        print(cat," a été enregistré avec succés!")

requestprod()
##    url = f'"{link}/1.json"'
