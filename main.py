import sys
import mysql.connector
import requests
import json
from constants import *
from classes.categories import Categories
from classes.products import Product
from classes.pur_beurre import Db
from classes.categoryproduct import Categoryproduct
from classes.substitutes import Substitute
from dbcreation import *

SELECTED_PRODUCT = []

try:
    """Try to connect to database."""
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor()
except mysql.connector.errors.ProgrammingError:
    """If database doesnt exist, creates it"""
    print("Database doesn't exist.\n"
    "Creating and filling database.\n")
    execsqlfile(mycursor, 'db.sql')
    requestcat()

def menu():
    """Choices to navigate in the program."""
    choice = input("Enter the number corresponding to the menu:\n"
    "1 : Manage substitutes.\n"
    "2 : Update database. (Delete all saved products.)\n"
    "Enter anything else to exit.\n")
    if choice == "1":
        subsMenu()
    elif choice == "2":
        execsqlfile(mycursor, 'db.sql')
        requestcat()
        print("Database up to date!")

    else:
        sys.exit()



def subsMenu():
    """Choices in substitute menu."""
    choice = input("1 : You want to find a new substitute.\n"
    "2 : You want to see your saved substitutes.\n"
    "3 : You want to delete saved substitutes.\n"
    "Enter anything else to exit.\n")
    if choice == "1":
        selectCat()
    elif choice == "2":
        if seeAllSubs() == 0:
            print("You have no saved substitutes.\n")
            back = input("Enter 1 to back. Anything else to exit.\n")
            if back == "1":
                subsMenu()
            else:
                sys.exit()
        else:
            input("Press any key to back.")
            subsMenu()
    elif choice == "3":
        if seeAllSubs() == 0:
            print("You have no saved substitutes.\n")
            back = input("Enter 1 to back. Anything else to exit.\n")
            if back == "1":
                subsMenu()
            else:
                sys.exit()
        choice = input("Enter the number corresponding to the substitute you want to delete.\n")
        Substitute.deleteSub(choice)
        input("Press any key to back.")
        subsMenu()
    else:
        sys.exit()

def selectCat():
    """Select a category."""
    for index, elem in enumerate(Categories.getAllCat()):
        print(str(index) + " : " + elem[0])
    choice = input("Chose your category.\n")
    try:
        choice = int(choice)
    except ValueError:
        print("Your entry is invalid.")
        input("Press any key to back to main menu.\n")
        menu()
    selectprod(choice)


def selectprod(choice):
    """Select the product you want to substitute."""
    global SELECTED_PRODUCT
    SELECTED_PRODUCT = []
    SELECTED_CATEGORY = None
    try:
        SELECTED_CATEGORY = Categories.getAllCat()[choice][0]
    except IndexError:
        print("The key you pressed doesn't correspond to any category.\n")
        input("Press any key to back to main menu.\n")
        menu()
    for index, elem in enumerate(Product.prodFromCat(SELECTED_CATEGORY)):
        print("Product number " + str(index) + " : \n"
        "Barcode : " + elem[0] + "\n"
        "Product name : " + str(elem[1]) + "\n"
        "Description : " + str(elem[2]) +  "\n"
        "OpenFoodFacts link : " + str(elem[3]) + "\n"
        "Store(s) : " + str(elem[4]) + "\n"
        "Nutriscore : " + str(elem[5]) + "\n\n")
    choiceprod = input("Chose the product you want to substitute.\n")
    try:
        choiceprod = int(choiceprod)
    except ValueError:
        print("Your entry is invalid.")
        input("Press any key to back to main menu.\n")
        menu()
    try:
        SELECTED_PRODUCT.append(Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][0])
    except IndexError:
        print("The key you pressed doesn't correspond to any product.\n")
        input("Press any key to back to main menu.\n")
        menu()
    if Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "a":
        print("The product you selected has the highest possible nutriscore. Please chose another one.\n")
        back = input("1 : Back to products.\n"
        "2 : Back to categories.\n"
        "Anything else to exit.\n")
        if back == "1":
            selectprod(choice)
        elif back == "2":
            selectCat()
        else:
            sys.exit()
    elif Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "b":
        selectsub(SELECTED_CATEGORY, b, choice)
    elif Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "c":
        selectsub(SELECTED_CATEGORY, c, choice)
    elif Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "d":
        selectsub(SELECTED_CATEGORY, d, choice)
    elif Product.prodFromCat(SELECTED_CATEGORY)[choiceprod][5] == "e":
        selectsub(SELECTED_CATEGORY, e, choice)
    else :
        print("The product you selected has no nutriscore. Please chose another one.")
        back = input("1 : Back to products.\n"
        "2 : Back to categories.\n"
        "Anything else to exit.\n")
        if back == "1":
            selectprod(choice)
        elif back == "2":
            selectCat()
        else:
            sys.exit()

def selectsub(category, nutriscore, choice):
    """Select the substitute and save it in database."""
    global SELECTED_PRODUCT
    if Product.allSubstitutes(category, nutriscore) == []:
        print("The product you selected has no higher nutriscore substitute. Please chose another one")
        back = input("1 : Back to products.\n"
        "2 : Back to categories.\n"
        "Anything else to exit.\n")
        if back == "1":
            selectprod(choice)
        elif back == "2":
            selectCat()
        else:
            sys.exit()
    for index, elem in enumerate(Product.allSubstitutes(category, nutriscore)):
        print("Product number " + str(index) + " : \n"
        "Barcode : " + elem[0] + "\n"
        "Product name : " + str(elem[1]) + "\n"
        "Description : " + str(elem[2]) +  "\n"
        "OpenFoodFacts link : " + str(elem[3]) + "\n"
        "Store(s) : " + str(elem[4]) + "\n"
        "Nutriscore : " + str(elem[5]) + "\n\n")
    choicesub = input("Select the substitute you want.\n")
    try:
        choicesub = int(choicesub)
    except ValueError:
        print("Your entry is invalid.")
        input("Press any key to back to main menu.\n")
        menu()
    try:
        SELECTED_PRODUCT.append(Product.allSubstitutes(category, nutriscore)[choicesub][0])
    except IndexError:
        print("The key you pressed doesn't correspond to any product.\n")
        input("Press any key to back to main menu.\n")
        menu()
    choicesave = input("Do you want to save them?\n"
    "1 : Yes.\n"
    "2 : No.\n")
    if choicesave == "1" :
        Substitute(SELECTED_PRODUCT[0],SELECTED_PRODUCT[1]).save()
        input("Press any key to back to main menu.\n")
        menu()
    else:
        sys.exit()



def seeAllSubs():
    """Display the saved substitutes."""
    i = 0
    for elem in Substitute.getAllSubstitute():
        i = i + 1
        print("Product substitued number "+ str(elem[0]) +":\n"
        "Barcode : " + str(Product.getOneProduct(elem[1])[0]) + "\n"
        "Product name : " + str(Product.getOneProduct(elem[1])[1]) + "\n"
        "Description : " + str(Product.getOneProduct(elem[1])[2]) +  "\n"
        "OpenFoodFacts link : " + str(Product.getOneProduct(elem[1])[3]) + "\n"
        "Store(s) : " + str(Product.getOneProduct(elem[1])[4]) + "\n"
        "Nutriscore : " + str(Product.getOneProduct(elem[1])[5]) + "\n\n"
        "Substitute number "+ str(elem[0]) +":\n"
        "Barcode : " + str(Product.getOneProduct(elem[2])[0]) + "\n"
        "Product name : " + str(Product.getOneProduct(elem[2])[1]) + "\n"
        "Description : " + str(Product.getOneProduct(elem[2])[2]) +  "\n"
        "OpenFoodFacts link : " + str(Product.getOneProduct(elem[2])[3]) + "\n"
        "Store(s) : " + str(Product.getOneProduct(elem[2])[4]) + "\n"
        "Nutriscore : " + str(Product.getOneProduct(elem[2])[5]) + "\n\n"
        )

if __name__ == '__main__':
    menu()
