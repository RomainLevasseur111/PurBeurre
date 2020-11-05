from constants import deletesave
from constants import selectcat
from constants import getallcats
from constants import getallsubs
from constants import getproductfromcat
from constants import insertsub
from constants import insertcatprod
from constants import insertcat
from constants import completeproduct
from constants import insertprod
from constants import PASSWORD
from constants import USER
from constants import HOST

import mysql.connector


class Db:
    connection = None

    @classmethod
    def getConnection(cls):
        """Connects to database if not connected."""
        if cls.connection is None:
            cls.dbconnect = mysql.connector.connect(
                host=HOST, user=USER, password=PASSWORD, database="pur_beurre"
            )
            cls.mycursor = cls.dbconnect.cursor(buffered=True)
            cls.connection = "connected"
        return cls.connection

    @classmethod
    def storeProducts(cls, array_tuple_product):
        cls.getConnection()
        """Checks if database is connected."""
        cls.mycursor.executemany(insertprod, array_tuple_product)
        """Executes a SQL request to store products."""
        cls.dbconnect.commit()
        """Saves changes"""

    @classmethod
    def getProduct(cls, barcode):
        cls.getConnection()
        cls.mycursor.execute(completeproduct, (barcode,))
        return cls.mycursor.fetchone()
        """Returns result of SQL request."""

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
        """Get all products from a category."""
        cls.getConnection()
        cls.mycursor.execute(getproductfromcat, (cat,))
        return cls.mycursor.fetchall()

    @classmethod
    def getSubstitute(cls, cat, nutri):
        """Returns all possible substitute of a product with same category
        and better nutriscore."""
        cls.getConnection()
        cls.mycursor.execute(nutri, (cat,))
        return cls.mycursor.fetchall()

    @classmethod
    def getAllSubs(cls):
        """Returns all saved substitutes."""
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
        """Returns one category."""
        cls.getConnection()
        cls.mycursor.execute(selectcat, (categoryid,))
        return cls.mycursor.fetchone()

    @classmethod
    def delSub(cls, idboth):
        """Deletes substitute."""
        cls.getConnection()
        cls.mycursor.execute(deletesave, (idboth,))
        cls.dbconnect.commit()
