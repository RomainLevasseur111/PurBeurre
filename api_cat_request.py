import requests
import mysql.connector
import json
from constants import *

def requestcat():
    url = "https://fr.openfoodfacts.org/categories.json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers = headers, data = payload)
    json_cat = response.json()
    tags_cat = json_cat.get('tags')[:NB_CATEGORY]
    name_cat = [(data.get('name'),) for data in tags_cat]
    sql = "INSERT IGNORE INTO categories (categoryname) VALUES (%s)"
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor()
    mycursor.executemany(sql, name_cat)
    connection.commit()
    mycursor.close()

requestcat()
