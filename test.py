import requests
import mysql.connector
import json
from constants import *

def test():
    connection = mysql.connector.connect(host=HOST,
                                         user=USER,
                                         password=PASSWORD,
                                         database='pur_beurre')
    mycursor = connection.cursor(buffered=True)

    sql = "SELECT categoryname FROM categories WHERE idcategory = 1"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    connection.commit()
    mycursor.close()
test()

"""
recupérer nom de cat pour ensuite donner un lien permettant de recuperer les
aliments dans cette categorie
"""
