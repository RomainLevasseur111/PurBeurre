from classes.pur_beurre import Db


class Product:
    def __init__(
        self, idbarcode, product_name, description, offlink, store,
            nutritiongrade):
        self.id_barcode = idbarcode
        self.product_name = product_name
        self.description = description
        self.offlink = offlink
        self.store = store
        self.nutritiongrade = nutritiongrade

    def __str__(self):
        return "{}"

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
        (
            idbarcode,
            product_name,
            description,
            offlink,
            store,
            nutritiongrade,
        ) = Db().getProduct(barcode)
        return (idbarcode, product_name, description, offlink, store,
                nutritiongrade)

    @staticmethod
    def prodFromCat(category):
        """Get all products from a category."""
        prods = []
        for elem in Db().getProdFromCat(category):
            prods.append(Product.getOneProduct(elem[0]))
        return prods

    @staticmethod
    def allSubstitutes(category, nutritiongrade):
        """Selects all possible substitute to a product that have same category
        and better nutriscore."""
        return Db().getSubstitute(category, nutritiongrade)
