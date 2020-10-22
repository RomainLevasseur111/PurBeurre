NB_CATEGORY = 5
NB_PAGEPRODUCT = 1
USER = 'OCP5'
HOST = 'localhost'
PASSWORD = ''
SELECTED_CATEGORY = []
SELECTED_PRODUCT = []

cat_link = "https://fr.openfoodfacts.org/categories.json"

insertcat = "INSERT IGNORE INTO categories (categoryname) VALUES (%s)"

insertprod = "INSERT IGNORE INTO products (idbarcode, productname, description, offlink, store, nutritiongrade) VALUES (%s, %s, %s, %s, %s, %s)"

insertcatprod = "INSERT IGNORE INTO categoryproduct (categoryname, idbarcode) VALUES (%s, %s)"

insertsub = "INSERT IGNORE INTO substitutes (idbarcode, idsubstitute) VALUES (%s, %s)"

getproductfromcat = "SELECT * FROM products INNER JOIN categoryproduct ON categoryproduct.idbarcode = products.idbarcode WHERE categoryname = %s"

e = "SELECT * FROM products INNER JOIN categoryproduct ON products.idbarcode = categoryproduct.idbarcode WHERE categoryname = %s AND products.nutritiongrade = 'd' OR 'c' OR 'b' OR 'a'"
d = "SELECT * FROM products INNER JOIN categoryproduct ON products.idbarcode = categoryproduct.idbarcode WHERE categoryname = %s AND products.nutritiongrade = 'c' OR 'b' OR 'a'"
c = "SELECT * FROM products INNER JOIN categoryproduct ON products.idbarcode = categoryproduct.idbarcode WHERE categoryname = %s AND products.nutritiongrade = 'b' OR 'a'"
b = "SELECT * FROM products INNER JOIN categoryproduct ON products.idbarcode = categoryproduct.idbarcode WHERE categoryname = %s AND products.nutritiongrade = 'a'"

completeproduct = "SELECT * FROM products WHERE idbarcode = %s"

getallsubs = "SELECT * FROM substitutes"

getallcats = "SELECT * FROM categories"

selectcat = "SELECT categoryname FROM categories WHERE categoryname = %s"
