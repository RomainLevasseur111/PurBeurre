import mysql.connector
from constants import *

connection = mysql.connector.connect(host=HOST,
                                     user=USER,
                                     password=PASSWORD)

mycursor = connection.cursor()
def execsqlfile(cursor, sql_file):

    statement = ""
    for line in open(sql_file):
        if line.strip().endswith(';') :
            statement = statement + line
            cursor.execute(statement)
            statement = ""
        else :
            statement = statement + line
    connection.commit()
    mycursor.close()
"""execsqlfile(mycursor, 'db.sql')"""
