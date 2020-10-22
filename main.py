import sys
import mysql.connector
import requests
import json
from constants import *
from testclass import *
from dbcreation import *
from api_request import *



try:
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor()
except mysql.connector.errors.ProgrammingError:
    print("La base de donnée est inexistante.\n"
    "Création et remplissage de la base de donnée...\n")
    execsqlfile(mycursor, 'db.sql')
    requestcat()

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
    choice = input("1 : You want to find a new substitute.\n"
    "2 : You want to see your saved substitutes.\n"
    "Enter anything else to exit.\n")
    if choice == "1":
        selectCat()
    elif choice == "2":
        for elem in Substitute.getAllSubstitute():
            print("Produit substitué numéro "+ str(elem[0]) +":\n"
            "Code barre : " + str(Product.getOneProduct(elem[1])[0]) + "\n"
            "Nom du produit : " + str(Product.getOneProduct(elem[1])[1]) + "\n"
            "Description : " + str(Product.getOneProduct(elem[1])[2]) +  "\n"
            "Lien OpenFoodFacts : " + str(Product.getOneProduct(elem[1])[3]) + "\n"
            "Magasins où l'acheter : " + str(Product.getOneProduct(elem[1])[4]) + "\n"
            "Nutriscore : " + str(Product.getOneProduct(elem[1])[5]) + "\n\n"
            "Substitut numéro "+ str(elem[0]) +":\n"
            "Code barre : " + str(Product.getOneProduct(elem[2])[0]) + "\n"
            "Nom du produit : " + str(Product.getOneProduct(elem[2])[1]) + "\n"
            "Description : " + str(Product.getOneProduct(elem[2])[2]) +  "\n"
            "Lien OpenFoodFacts : " + str(Product.getOneProduct(elem[2])[3]) + "\n"
            "Magasins où l'acheter : " + str(Product.getOneProduct(elem[2])[4]) + "\n"
            "Nutriscore : " + str(Product.getOneProduct(elem[2])[5]) + "\n\n"
            )
    else:
        sys.exit()

def selectCat():

    for index, elem in enumerate(Categories.getAllCat()):
        print(str(index) + " : " + elem[0])
    choice = input("Chose your category.\n")
    choice = int(choice)
    SELECTED_CATEGORY = Categories.getAllCat()[choice][0]
    for index, elem in enumerate(Product.prodFromCat(SELECTED_CATEGORY)):
        print("Produit numéro " + str(index) + " : \n"
        "Code barre : " + elem[0] + "\n"
        "Nom du produit : " + str(elem[1]) + "\n"
        "Description : " + str(elem[2]) +  "\n"
        "Lien OpenFoodFacts : " + str(elem[3]) + "\n"
        "Magasins où l'acheter : " + str(elem[4]) + "\n"
        "Nutriscore : " + str(elem[5]) + "\n\n")
    choiceprod = input("Chose the product you want to substitute.\n")
    choiceprod = int(choiceprod)
    SELECTED_PRODUCT.append(Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][0])
    if Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "a":
        print("The product you selected has the highest possible nutriscore. Please chose another one.")
        quit()
    elif Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "b":
        selectsub(SELECTED_CATEGORY, b)
    elif Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "c":
        selectsub(SELECTED_CATEGORY, c)
    elif Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "d":
        selectsub(SELECTED_CATEGORY, d)
    elif Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "e":
        selectsub(SELECTED_CATEGORY, e)
    else :
        print("The product you selected has no nutriscore. Please chose another one.")


def selectsub(category, nutriscore):
    for index, elem in enumerate(Product.allSubstitutes(category, nutriscore)):
        print("Produit numéro " + str(index) + " : \n"
        "Code barre : " + elem[0] + "\n"
        "Nom du produit : " + str(elem[1]) + "\n"
        "Description : " + str(elem[2]) +  "\n"
        "Lien OpenFoodFacts : " + str(elem[3]) + "\n"
        "Magasins où l'acheter : " + str(elem[4]) + "\n"
        "Nutriscore : " + str(elem[5]) + "\n\n")
    choice = input("Select the substitute you want.\n")
    choice = int(choice)
    SELECTED_PRODUCT.append(Product.allSubstitutes(category, nutriscore)[choice][0])
    choice = input("Do you want to save them?\n"
    "1 : Yes.\n"
    "2 : No.\n")
    if choice == "1" :
        Substitute(SELECTED_PRODUCT[0],SELECTED_PRODUCT[1]).save()
    else:
        sys.exit()
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
