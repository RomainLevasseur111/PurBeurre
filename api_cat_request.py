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
    tags_cat = json_cat.get('tags')
    name_cat = [data.get('name') for data in tags_cat]
    sql = "INSERT INTO categories (categoryname) VALUES (%s)"
    i = 2
    connection = mysql.connector.connect(host='localhost',
                                         user='OCP5',
                                         password='password',
                                         database='pur_beurre')
    while i < (NB_CATEGORY + 2) :
        mycursor = connection.cursor()
        mycursor.execute(sql, name_cat)
        connection.commit()
        mycursor.close()
        i = i + 1
requestcat()
