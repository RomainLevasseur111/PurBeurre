import requests
import mysql.connector
import json
from constants import *

def requestprod():
    url = "https://fr.openfoodfacts.org/api/v2/produit/3478820600651"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers = headers, data = payload)
    json_prod = response.json()
    products_prod = json_prod.get('product')
    prod_name = products_prod.get('product_name')
    prod_desc = products_prod.get('generic_name')
    prod_url = products_prod.get('url')
    prod_stores = products_prod.get('stores')
    prod_code = products_prod.get('id')
    prod_nutri = products_prod.get('nutriscore_grade')
    prod_data = (prod_name, prod_desc, prod_url, prod_stores, prod_code, prod_nutri)
    sql = "INSERT INTO products (productname, description, offlink, store, barcode, nutritiongrade) VALUES (%s, %s, %s, %s, %s, %s)"
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor()
    mycursor.execute(sql, prod_data)
    connection.commit()
    mycursor.close()
requestprod()


"""
"INSERT INTO products" "(productname, description, offlink, store, barcode, nutritiongrade, bio)" "VALUES()"
"product_name" "generic_name" "url" "stores" "id" "nutriscore_grade"
"""
