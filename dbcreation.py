import mysql.connector
from constants import *

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
