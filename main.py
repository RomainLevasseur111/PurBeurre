import mysql.connector
import requests
import json
from constants import *
"""from testclass import *"""
from dbcreation import *

try:
    connection = mysql.connector.connect(host=HOST,
                                 user=USER,
                                 password=PASSWORD,
                                 database='pur_beurre')

    mycursor = connection.cursor()
except mysql.connector.errors.ProgrammingError:
    print("Database doesn't exist.")
    print("Creating Database")
    execsqlfile(mycursor,'db.sql')





"""
lance le programme
essaie de se connecter à la bdd
si inexistante : dbcreation.py puis se connecte
api_cat_request.py
stocker la cat lors du choix de l'utilisateur

"""
