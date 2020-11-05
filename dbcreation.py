import mysql.connector
from constants import NB_CATEGORY, NB_PAGEPRODUCT, cat_link, PASSWORD, USER, HOST
from classes.categories import Categories
from classes.products import Product
from classes.categoryproduct import Categoryproduct
import requests
import json

connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)

mycursor = connection.cursor()


def execsqlfile(sql_file):
    """Reads and executes instructions of a .sql file."""
    statement = ""
    for line in open(sql_file):
        if line.strip().endswith(";"):
            statement = statement + line
            mycursor.execute(statement)
            statement = ""
        else:
            statement = statement + line
    connection.commit()
    mycursor.close()


def requestprod(cat, link):
    """Save products in the database."""
    i = 1
    urls = []
    """Saving number of pages."""
    while i < NB_PAGEPRODUCT + 1:
        urls.append(link + "/" + str(i))
        i += 1
    """For each page of a catagory from OpenFoodFacts, takes data of all fields.
    (id product_name...) Then creates a Product object and save it in
    database."""
    for l in urls:
        response = requests.request("GET", l + ".json")
        json_prod = response.json()
        products_prod = json_prod.get("products")
        prod_info = [
            Product(
                data.get("id"),
                data.get("product_name"),
                data.get("generic_name"),
                data.get("url"),
                data.get("stores"),
                data.get("nutriscore_grade"),
            )for data in products_prod
        ]
        product_barcode = [(data.get("id"),) for data in products_prod]
        """Fills Categoryproduct table."""
        for elem in product_barcode:
            catprod = Categoryproduct(cat, elem[0])
            catprod.save()
        Product.saveMany(prod_info)


def requestcat():
    """Takes categories names et urls."""
    response = requests.request("GET", cat_link)
    json_cat = response.json()
    tags_cat = json_cat.get("tags")[:NB_CATEGORY]
    name_cat = [(data.get("name"),) for data in tags_cat]
    link_cat = [(data.get("url"),) for data in tags_cat]
    categories = [Categories(elem[0]) for elem in name_cat]
    """Creates a Categories object with names and save it in database."""
    Categories.saveMany(categories)
    """For each urls, calls requestprod."""
    for index, cat in enumerate(name_cat):
        requestprod(cat[0], link_cat[index][0])
