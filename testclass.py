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
            cls.mycursor = cls.dbconnect.cursor(buffered=True)
            cls.connection = "connected"
            print("Db connected")
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
        cls.mycursor.execute(getsub,(cat, nutri))
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

class Product:
    def __init__(self, idbarcode, product_name, description, offlink, store, nutritiongrade):
        self.id_barcode = idbarcode
        self.product_name = product_name
        self.description = description
        self.offlink = offlink
        self.store = store
        self.nutritiongrade = nutritiongrade

    """def __repr__(self):
        return str(Product(idbarcode, product_name, description, offlink, store, nutritiongrade))"""

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
    def getOneProduct(barcode):
        (productid, idbarcode, product_name, description, offlink, store, nutritiongrade) = Db().getProduct(barcode)
        return Product(idbarcode, product_name, description, offlink, store, nutritiongrade)

    @staticmethod
    def prodFromCat(category):
        listofproducts = [Db().getProdFromCat(category)]
        print(listofproducts)

    @staticmethod
    def allSubstitutes(category, nutritiongrade):
        listofpossiblesub = [Db().getSubstitute(category, nutritiongrade)]
        for elem in listofpossiblesub:
            print(elem)

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
    def getAllCat():
        for elem in Db().getAllCategories():
            print(elem)


class Categoryproduct:
    def __init__ (self, categoryname, idbarcode):
        self.categoryname =  categoryname
        self.idbarcode = idbarcode

    def toTuple(self):
        return(
            self.categoryname,
            self.idbarcode,
        )

    def save(self):
        Db().storeCatProd([self.toTuple()])

    @staticmethod
    def saveMany(many_catprod):
        values = [elem.toTuple() for elem in many_catprod]
        Db().storeCatProd(values)


class Substitute:
    def __init__ (self, idbarcode, idsubstitute):
        self.idbarcode = idbarcode
        self.idsubstitute = idsubstitute

    def toTuple(self):
        return(
            self.idbarcode,
            self.idsubstitute
        )

    def save(self):
        Db().storeSub([self.toTuple()])

    @staticmethod
    def saveMany(many_sub):
        values = [elem.toTuple() for elem in many_sub]
        Db().storeSub(values)

    @staticmethod
    def getOneSubstitute(idsub, idprod):
        ids = Db().getProduct(idsub)
        idp = Db().getProduct(idprod)
        return [Product(),Product()]

    def getAllSubstitute():
        print(Db().getAllSubs())
