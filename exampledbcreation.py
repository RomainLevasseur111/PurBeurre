import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             db='database_name',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try :
    with connection.cursor() as cursor:
        sql = "CREATE TABLE categoryproduct (idcategory INT NOT NULL, idproduct INT NOT NULL);"
        cursor.execute(sql)
    connection.commit()

finally :
    connection.close()
