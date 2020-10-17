from pur_beurre import *

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
