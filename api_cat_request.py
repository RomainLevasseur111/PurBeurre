import requests
import mysql.connector
from constants import *

def requestcat():
    url_cat = requests.get("https://fr.openfoodfacts.org/categories.json")
    cat_json = url_cat.json()
    cat_tags = cat_json.get('tags')
    data_cat_name = [d.get('name') for d in cat_tags]
    i=2
    while i < (NB_CATEGORY + 2) :

        connection = mysql.connector.connect(host='localhost',
                                             user='OCP5',
                                             password='password',
                                             database='pur_beurre')
        mycursor = connection.cursor()
        mycursor.execute("INSERT IGNORE INTO categories" "(categoryname)" "VALUES('{}')".format(data_cat_name[i]))
        connection.commit()
        mycursor.close()
        i = i + 1
requestcat()
