import sys
import mysql.connector
import requests
import json
from constants import *
from testclass import *
"""from dbcreation import *"""



def menu():
    choice = input("Enter the number corresponding to the menu:\n"
    "1 : Find a substitute.\n"
    "2 : Manage database.\n"
    "Enter anything else to exit.\n")
    if choice == "1":
        subsMenu()
    elif choice == "2":
        print("qqc")

    else:
        sys.exit()



def subsMenu():
    choice = input("1 - You want to find a new substitute.\n"
    "2 - You want to see your saved substitutes.\n"
    "Enter anything else to exit.\n")
    if choice == "1":
        selectCat()
    elif choice == "2":
        Substitute.getAllSubstitute()
    else:
        sys.exit()

def selectCat():
    Categories.getAllCat()
    choice = input("Chose your category.\n")
    
menu()


"""1er screen 2 choix
1:substituer
    2 choix:
    1trouver un sub
        choisir catégorie
            choisir produit
    2voir les sub svg
2gerer bdd
    1 maj bdd
    2reinit bdd
    3 sup elem svg"""


"""
lance le programme
essaie de se connecter à la bdd
si inexistante : dbcreation.py puis se connecte
api_cat_request.py
stocker la cat lors du choix de l'utilisateur

"""
