NB_CATEGORY = 1
NB_PAGEPRODUCT = 1
USER = 'OCP5'
HOST = 'localhost'
PASSWORD = ''
cat_link = "https://fr.openfoodfacts.org/categories.json"

insertcat = "INSERT IGNORE INTO categories (categoryname) VALUES (%s)"

insertprod = "INSERT IGNORE INTO products (idbarcode, productname, description, offlink, store, nutritiongrade) VALUES (%s, %s, %s, %s, %s, %s)"

insertcatprod = "INSERT IGNORE INTO categoryproduct (categoryname, idbarcode) VALUES (%s, %s)"

insertsub = "INSERT IGNORE INTO substitute (idboth, idbarcode, idsubstitute) VALUES (%s, %s, %s)"
