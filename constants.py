# Parameters
NB_CATEGORY = 1
NB_PAGEPRODUCT = 1
USER = "OCP5"
HOST = "localhost"
PASSWORD = ""

# Link to openfoodfacts categories
cat_link = "https://fr.openfoodfacts.org/categories.json"

# SQL requests
insertcat = "INSERT IGNORE INTO categories (categoryname) VALUES (%s)"

insertprod = ("INSERT IGNORE INTO products (idbarcode, productname, description, offlink, store, nutritiongrade) VALUES (%s, %s, %s, %s, %s, %s)")

insertcatprod = ("INSERT IGNORE INTO categoryproduct (categoryname, idbarcode"
                 ") VALUES (%s, %s)")

insertsub = ("INSERT IGNORE INTO substitutes (idbarcode, idsubstitute) VALUE"
             "S (%s, %s)")

getproductfromcat = ("SELECT * FROM products INNER JOIN categoryproduct ON"
                     " categoryproduct.idbarcode = products.idbarcode WHERE"
                     " categoryname = %s")

e = ("SELECT * FROM products INNER JOIN categoryproduct ON products.idbarco"
     "de = categoryproduct.idbarcode WHERE categoryname = %s AND (products"
     ".nutritiongrade = 'd' OR products.nutritiongrade = 'c' OR products.n"
     "utritiongrade = 'b' OR products.nutritiongrade = 'a')")
d = ("SELECT * FROM products INNER JOIN categoryproduct ON products.idbarc"
     "ode = categoryproduct.idbarcode WHERE categoryname = %s AND (product"
     "s.nutritiongrade = 'c' OR products.nutritiongrade = 'b' OR products."
     "nutritiongrade = 'a')")
c = ("SELECT * FROM products INNER JOIN categoryproduct ON products.idbarc"
     "ode = categoryproduct.idbarcode WHERE categoryname = %s AND (product"
     "s.nutritiongrade = 'b' OR products.nutritiongrade = 'a')")
b = ("SELECT * FROM products INNER JOIN categoryproduct ON products.idbarc"
     "ode = categoryproduct.idbarcode WHERE categoryname = %s AND products"
     ".nutritiongrade = 'a'")

completeproduct = "SELECT * FROM products WHERE idbarcode = %s"

getallsubs = "SELECT * FROM substitutes"

getallcats = "SELECT * FROM categories"

selectcat = "SELECT categoryname FROM categories WHERE categoryname = %s"

deletesave = "DELETE FROM substitutes WHERE idboth = %s"
