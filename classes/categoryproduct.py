from pur_beurre import *

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
