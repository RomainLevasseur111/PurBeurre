NB_CATEGORY = 20
NB_PAGEPRODUCT = 50
USER = 'OCP5'
HOST = 'localhost'
PASSWORD = ''
cat_link = "https://fr.openfoodfacts.org/categories.json"

insertcat = "INSERT IGNORE INTO categories (categoryname) VALUES (%s)"

insertprod = "INSERT IGNORE INTO products (idbarcode, productname, description, offlink, store, nutritiongrade) VALUES (%s, %s, %s, %s, %s, %s)"
