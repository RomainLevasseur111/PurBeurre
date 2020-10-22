from constants import *
import mysql.connector

class Db:
    connection = None

    @classmethod
    def getConnection(cls):
        if cls.connection == None:
            cls.dbconnect = mysql.connector.connect(host=HOST,
                                                user=USER,
                                                password=PASSWORD,
                                                database='pur_beurre')
            cls.mycursor = cls.dbconnect.cursor(buffered=True)
            cls.connection = "connected"
        return cls.connection

    @classmethod
    def storeProducts(cls, array_tuple_product):
        cls.getConnection()
        cls.mycursor.executemany(insertprod, array_tuple_product)
        cls.dbconnect.commit()

    @classmethod
    def getProduct(cls, barcode):
        cls.getConnection()
        cls.mycursor.execute(completeproduct, (barcode,))
        return cls.mycursor.fetchone()

    @classmethod
    def storeCategories(cls, array_tuple_category):
        cls.getConnection()
        cls.mycursor.executemany(insertcat, array_tuple_category)
        cls.dbconnect.commit()

    @classmethod
    def storeCatProd(cls, array_tuple_catprod):
        cls.getConnection()
        cls.mycursor.executemany(insertcatprod, array_tuple_catprod)
        cls.dbconnect.commit()

    @classmethod
    def storeSub(cls, array_tuple_sub):
        cls.getConnection()
        cls.mycursor.executemany(insertsub, array_tuple_sub)
        cls.dbconnect.commit()

    @classmethod
    def getProdFromCat(cls, cat):
        cls.getConnection()
        cls.mycursor.execute(getproductfromcat, (cat,))
        return cls.mycursor.fetchall()

    @classmethod
    def getSubstitute(cls, cat, nutri):
        cls.getConnection()
        cls.mycursor.execute(nutri, (cat,))
        return cls.mycursor.fetchall()

    @classmethod
    def getAllSubs(cls):
        cls.getConnection()
        cls.mycursor.execute(getallsubs)
        return cls.mycursor.fetchall()

    @classmethod
    def getAllCategories(cls):
        cls.getConnection()
        cls.mycursor.execute(getallcats)
        return cls.mycursor.fetchall()

    @classmethod
    def selectCat(cls, categoryid):
        cls.getConnection()
        cls.mycursor.execute(selectcat, (categoryid,))
        return cls.mycursor.fetchone()

    @classmethod
    def delSub(cls, idboth):
        cls.getConnection()
        cls.mycursor.execute(deletesave, (idboth,))
        cls.dbconnect.commit()
