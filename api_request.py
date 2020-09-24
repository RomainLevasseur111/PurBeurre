import requests
import mysql.connector
import json
from constants import *
from testclass import *

def requestprod(link):
    i = 1
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
        product = Product(prod_code)
        product.saveMany()

def prodcat(cat, link):
    i = 1
    urls = []
    while i < NB_PAGEPRODUCT + 1:
        urls.append(link+"/"+str(i))
        i += 1
    for l in urls :
        response = requests.request("GET", l+".json")
        json_prod = response.json()
        products_prod = json_prod.get('products')
        product_code = [(data.get('id'),)for data in products_prod]
        for elem in product_code :
            catprod = Categoryproduct((cat, elem[0]))
            catprod.save()

def requestcat():

    response = requests.request("GET", cat_link)
    json_cat = response.json()
    tags_cat = json_cat.get('tags')[:NB_CATEGORY]
    name_cat = [(data.get('name'),) for data in tags_cat]
    link_cat = [(data.get('url'),) for data in tags_cat]
    for link in link_cat :
        requestprod(link[0])
    for cat in name_cat:
        category = Categories(cat[0])
        category.saveCat()
    """for cat in name_cat :
        for link in link_cat :
            prodcat(cat[0], link[0])"""
requestcat()
