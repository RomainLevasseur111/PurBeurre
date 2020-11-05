from classes.pur_beurre import Db


class Categories:
    def __init__(self, categoryname):
        self.categoryname = categoryname

    def __str__(self):
        return "{}"

    def toTuple(self):
        """Changes object parameters into a tuple."""
        return (self.categoryname,)

    def saveCat(self):
        """Saves object into database using Db class."""
        Db().storeCategories([self.toTuple()])

    @staticmethod
    def saveMany(many_categories):
        """Saves multiple objects at once."""
        values = [elem.toTuple() for elem in many_categories]
        Db().storeCategories(values)

    @staticmethod
    def getAllCat():
        """Get all catagories."""
        return Db().getAllCategories()

    @classmethod
    def getOneCat(self, categoryid):
        """Get one category."""
        (categoryname) = Db().selectCat(categoryid)
        return categoryname[0]
