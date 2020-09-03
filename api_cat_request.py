import requests
import mysql.connector
import json
from constants import *

def requestprod(link):
    url = f'"{link}.json"'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers = headers, data = payload)
    json_prod = response.json()
    products_prod = json_prod.get('products')[:NB_PRODUCT]
    prod_code = [(data.get('id'),) for data in products_prod]
    prod_name = [(data.get('product_name'),) for data in products_prod]
    prod_desc = [(data.get('generic_name'),) for data in products_prod]
    prod_url = [(data.get('url'),) for data in products_prod]
    prod_stores = [(data.get('stores'),) for data in products_prod]
    prod_nutri = [(data.get('nutriscore_grade'),) for data in products_prod]
    prod_data = (prod_code, prod_name, prod_desc, prod_url, prod_stores, prod_nutri)
    sql = "INSERT INTO products (idbarcode, productname, description, offlink, store, nutritiongrade) VALUES (%s, %s, %s, %s, %s, %s)"
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor()
    mycursor.executemany(sql, prod_data)
    connection.commit()
    mycursor.lastrowid()
    mycursor.close()

def requestcat():
    url = "https://fr.openfoodfacts.org/categories.json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers = headers, data = payload)
    json_cat = response.json()
    tags_cat = json_cat.get('tags')[:NB_CATEGORY]
    name_cat = [(data.get('name'),) for data in tags_cat]
    link_cat = [(data.get('url'),) for data in tags_cat]
    for link in link_cat :
        print(link[0])
        requestprod(link[0])
    """
    sql = "INSERT IGNORE INTO categories (categoryname) VALUES (%s)"
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor()
    mycursor.executemany(sql, name_cat)
    connection.commit()
    mycursor.close()"""

requestcat()
