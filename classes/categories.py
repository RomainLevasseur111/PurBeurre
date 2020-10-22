from classes.pur_beurre import *

class Categories:
    def __init__(self, categoryname):
        self.categoryname = categoryname

    def __str__(self):
        return "{}"

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
        return Db().getAllCategories()


    @classmethod
    def getOneCat(self, categoryid):
        (categoryname) = Db().selectCat(categoryid)
        return (categoryname[0])
