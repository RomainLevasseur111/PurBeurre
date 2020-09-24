import requests
import mysql.connector
import json
from constants import *
from testclass import *

def requestprod(cat, link):
    i = 1
    urls = []
    while i < NB_PAGEPRODUCT + 1:
        urls.append(link+"/"+str(i))
        i += 1
    for l in urls :
        response = requests.request("GET", l+".json")
        json_prod = response.json()
        products_prod = json_prod.get('products')
        prod_info = [(data.get('id'), data.get('product_name'), data.get('generic_name'), data.get('url'), data.get('stores'), data.get('nutriscore_grade')) for data in products_prod]
        product_barcode = [(data.get('id'),)for data in products_prod]
        for elem in product_barcode :
            catprod = Categoryproduct(cat, elem[0])
            catprod.save()
        product = Product(prod_info)
        product.saveMany()
        for elem in prod_info:
            (elem,) = elem
            print(elem)
            product = Product(elem)
            product.saveMany()

def requestcat():

    response = requests.request("GET", cat_link)
    json_cat = response.json()
    tags_cat = json_cat.get('tags')[:NB_CATEGORY]
    name_cat = [(data.get('name'),) for data in tags_cat]
    link_cat = [(data.get('url'),) for data in tags_cat]
    for cat in name_cat:
        category = Categories(cat[0])
        category.saveCat()
    for cat in name_cat :
        for link in link_cat :
            requestprod(cat[0], link[0])
requestcat()
