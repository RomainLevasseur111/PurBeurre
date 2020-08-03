import pymysql.cursors
from execsqlfile import *

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             db='database_name',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try :
    with connection.cursor() as cursor:
        execsqlfile(cursor, 'request.sql')
    connection.commit()

finally :
    connection.close()
