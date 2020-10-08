NB_CATEGORY = 6
NB_PAGEPRODUCT = 1
USER = 'OCP5'
HOST = 'localhost'
PASSWORD = ''
selected_category = ['Snacks']
selected_product = []

cat_link = "https://fr.openfoodfacts.org/categories.json"

insertcat = "INSERT IGNORE INTO categories (categoryname) VALUES (%s)"

insertprod = "INSERT IGNORE INTO products (idbarcode, productname, description, offlink, store, nutritiongrade) VALUES (%s, %s, %s, %s, %s, %s)"

insertcatprod = "INSERT IGNORE INTO categoryproduct (categoryname, idbarcode) VALUES (%s, %s)"

insertsub = "INSERT IGNORE INTO substitutes (idbarcode, idsubstitute) VALUES (%s, %s)"

getproductfromcat = "SELECT * FROM products INNER JOIN categoryproduct ON categoryproduct.idbarcode = products.idbarcode WHERE categoryname = %s"

getsub =  "SELECT * FROM products INNER JOIN categoryproduct ON products.idbarcode = categoryproduct.idbarcode WHERE categoryproduct.categoryname = %s AND products.nutritiongrade = %s"

completeproduct = "SELECT * FROM products WHERE idbarcode = %s"
