# Pur Beurre
## Utilisation des données publiques d'OpenFoodFacts

La startup Pur Beurre nous demande de créer un programme interagissant avec la base de données d'OpenFoodFacts afin d'en __récupérer les aliments__ et leurs descriptions, et de donner la possibilité aux utilisateurs de lui __trouver un substitut__.


### Installation and launch program
Git clone the files.
"pip install -r requirements.txt" in command prompt to install needed packages.
Change constants.py parameters to your convenience.
Type python main.py in command prompt to start the program.


### Description
If the database doesn't exist, the program creates and fills it automatically when launch

User as two options :
  1. "Manage substitutes."

  2. "Update database. (Delete all saved products.)"

If user chose "Manage substitutes", he has 3 new options :
  1. "You want to find a new substitute."

  2. "You want to see your saved substitutes."

  3. "You want to delete saved substitutes".

If user chose "You want to find a new substitute.", he has to chose first a substitute, then the product he wants to substitute.
Program gives all possible substitutes.
Eventually, user chose the substitutes he wants and has the possibility to save it into the database.
