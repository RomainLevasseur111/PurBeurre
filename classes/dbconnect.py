import mysql.connector

class Dbconnect :
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        '''self.connect = Null'''
    def connect(self):
        connection = mysql.connector.connect(host=self.host,
                                            user=self.user,
                                            password=self.password,
                                            database=self.db)
        mycursor = connection.cursor()
