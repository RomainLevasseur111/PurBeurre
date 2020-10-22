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
        prod_info = [Product(data.get('id'), data.get('product_name'), data.get('generic_name'), data.get('url'), data.get('stores'), data.get('nutriscore_grade')) for data in products_prod]
        product_barcode = [(data.get('id'),)for data in products_prod]
        for elem in product_barcode :
            catprod = Categoryproduct(cat, elem[0])
            catprod.save()
        Product.saveMany(prod_info)


def requestcat():

    response = requests.request("GET", cat_link)
    json_cat = response.json()
    tags_cat = json_cat.get('tags')[:NB_CATEGORY]
    name_cat = [(data.get('name'),) for data in tags_cat]
    link_cat = [(data.get('url'),) for data in tags_cat]
    categories = [Categories(elem[0]) for elem in name_cat]
    Categories.saveMany(categories)
    for index, cat in enumerate(name_cat) :
        requestprod(cat[0], link_cat[index][0])
