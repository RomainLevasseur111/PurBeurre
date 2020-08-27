import mysql.connector
import requests
import json
import constants as constants


"""
lance le programme
essaie de se connecter à la bdd
si inexistante : dbcreation.py puis se connecte
api_cat_request.py
recupérer nom de cat pour ensuite donner un lien permettant de recuperer les
aliments dans cette categorie
boucle api_prod_request.py pour les NB_PRODUCT de chaque categorie

"""
