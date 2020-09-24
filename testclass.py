import requests
import mysql.connector
import json
from constants import *

class Db:
    connection = None
    dbconnect = mysql.connector.connect(host=HOST,
                                        user=USER,
                                        password=PASSWORD,
                                        database='pur_beurre')
    mycursor = None

    @classmethod
    def getConnection(cls):
        if cls.connection == None:
            cls.mycursor = cls.dbconnect.cursor()
            cls.connection = "connected"
            print("Db connected")
        return cls.connection

    @classmethod
    def storeProducts(cls, array_tuple_product):
        cls.getConnection()
        cls.mycursor.executemany(insertprod, array_tuple_product)
        cls.dbconnect.commit()
        #print('db.storeProducts:',array_tuple_product)

    @classmethod
    def getProduct(cls, id):
        cls.getConnection()
        print('db.getProduct:',id)

    @classmethod
    def storeCategories(cls, array_tuple_category):
        cls.getConnection()
        cls.mycursor.executemany(insertcat, array_tuple_category)
        cls.dbconnect.commit()
        #print('db.storeCategories:',array_tuple_category)

    @classmethod
    def getCategory(cls, id):
        pass

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


class Product:
    def __init__(self, idbarcode, product_name, description, offlink, store, nutritiongrade):
        self.id_barcode = idbarcode
        self.product_name = product_name
        self.description = description
        self.offlink = offlink
        self.store = store
        self.nutritiongrade = nutritiongrade

    def toTuple(self):
        return (
            self.id_barcode,
            self.product_name,
            self.description,
            self.offlink,
            self.store,
            self.nutritiongrade,
        )

    def save(self):
        Db().storeProducts([self.toTuple()])

    @staticmethod
    def saveMany(many_product):
        values = [elem.toTuple() for elem in many_product]
        Db().storeProducts(values)

    @staticmethod
    def getOneProduct(id):
        tps = Db().getProduct(id)
        return Product(11,11,11,11,11,11)



class Categories:
    def __init__(self, categoryname):
        self.categoryname = categoryname

    def toTuple(self):
        return (
            self.categoryname,
        )

    def saveCat(self):
        Db().storeCategories([self.toTuple()])

    @staticmethod
    def saveMany(many_categories):
        values = [elem.toTuple() for elem in many_categories]
        Db().storeCategories(values)

    @staticmethod
    def getOneCategory(id):
        tps = Db().getCategory(id)
        return Categories(11)


class Categoryproduct:
    def __init__ (self, categoryname, idbarcode):
        self.categoryname =  categoryname
        self.idbarcode = idbarcode

    def toTuple(self):
        return(
            self.categoryname,
            self.idbarcode
        )

    def save(self):
        Db().storeCatProd([self.toTuple()])

    @staticmethod
    def saveMany(many_catprod):
        values = [elem.toTuple() for elem in many_catprod]
        Db().storeCatProd(values)


class Substitute:
    def __init__ (self, idboth, idbarcode, idsubstitute):
        self.idboth = idboth
        self.idbarcode = idbarcode
        self.idsubstitute = idsubstitute

    def toTuple(self):
        return(
            self.idboth,
            self.idbarcode,
            self.idsubstitute
        )

    def save(self):
        Db().storeCatProd([self.toTuple()])

    @staticmethod
    def saveMany(many_sub):
        values = [elem.toTuple() for elem in many_sub]
        Db().storeSub(values)


test1 = Categories("coucou")
test1.saveCat()
test2 = Categories("salut")
test3 = Categories("bonjour")
Categories.saveMany([test2,test3])


test = Product(1,2,3,4,5,6)
test2 = Product('A','B','C','D','E','F')
test3 = Product(7,8,9,10,11,2)
Product.saveMany([test, test2, test3])

test4 = Product.getOneProduct(123456789)

test1 = Categoryproduct("salut", "8645")
test1.save()

test2 = Categoryproduct("bonjour","4556")
test3 = Categoryproduct("hello", "65848")
Categoryproduct.saveMany([test2, test3])
