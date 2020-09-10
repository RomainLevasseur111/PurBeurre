import mysql.connector
import requests
import json
import constants as constants
from dbcreation import *

try:
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor()
except :
    connection = mysql.connector.connect(host=HOST,
                                 user=USER,
                                 password=PASSWORD)

    mycursor = connection.cursor()
    execsqlfile(mycursor, 'db.sql')












"""
lance le programme
essaie de se connecter à la bdd
si inexistante : dbcreation.py puis se connecte
api_cat_request.py
recupérer nom de cat pour ensuite donner un lien permettant de recuperer les
aliments dans cette categorie
boucle api_prod_request.py pour les NB_PRODUCT de chaque categorie

"""
