"""
    #Créez un nouveau fichier Python et nommez-le "products.py".
    #Définissez la classe Product avec ses attributs cost, price, et marque dans la méthode init.
    #Définissez la classe Meubles en tant que sous-classe de la classe Product, en utilisant le mot-clé "class Meubles(Product):".
    #Définissez la méthode init de la classe Meubles en appelant la méthode init de la classe parent avec le super().init(cost, price, marque).
    #Ajoutez les attributs spécifiques à la classe Meubles, tels que les matériaux, la couleur et les dimensions.
    #Répétez les étapes 3 à 5 pour les classes Canape, Chaise et Table.
    #Vous pouvez maintenant utiliser ces classes pour créer des instances de meubles spécifiques dans votre programme principal.
"""

class Products :
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque 

    def afficher_carac(self):
        print('les caracteristique sont : ')
        print('cost: ',self.cost)
        print('price: ',self.price)
        print('marque: ',self.marque)


class Meubles(Products) : 
    def __init__(self, cost, price, marque, materiau, couleur, dimensions) :
        super().__init__(cost, price, marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimensions = dimensions

    def afficher_carac(self):
        super().afficher_carac()
        print('materiaux: ',self.materiau)
        print('couleur: ',self.couleur)
        print('dimensions: ',self.dimensions)


class Canape(Products) :
    def __init__(self, cost, price, marque, materiau, couleur, dimensions, nom) :
        super().__init__(cost, price, marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimensions = dimensions
        self.nom = nom
           
    def afficher_carac(self):
        super().afficher_carac()
        print('materiau: ',self.materiau)
        print('couleur: ',self.couleur)
        print('dimensions: ',self.dimensions)
        print('nom : ',self.nom)


class Chaise(Products) :
    def __init__(self, cost, price, marque, materiau, couleur, dimensions, nom) :
        super().__init__(cost, price, marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimensions = dimensions
        self.nom = nom


    def afficher_carac(self):
        super().afficher_carac()
        print('materiaux: ',self.materiau)
        print('couleur: ',self.couleur)
        print('dimensions: ',self.dimensions)
        print('nom : ',self.nom)


class Table(Products) :
    def __init__(self, cost, price, marque, materiau, couleur, dimensions) :
        super().__init__(cost, price, marque)
        self.materiau = materiau
        self.couleur = couleur
        self.dimensions = dimensions

    def afficher_carac(self):
        super().afficher_carac()
        print('materiaux: ',self.materiau)
        print('couleur: ',self.couleur)
        print('dimensions: ',self.dimensions)


canape1 = Canape(1000,2000,"OKLM", "cuir", "Blanc", "200x100x80", "Canape") 
canape2 = Canape(800,1600,"SIESTA","Tissu","Bleu","150x90x70","Canape")
chaise1 = Chaise(50,100,"PEPOUSE","Plastique","Rouge","50x50x70","Chaise") 
chaise2 = Chaise(75,150,"PEPOUSE","Métal","Gris","60x60x80","Chaise")
table2 = Table(250,500,"TEX","Bois","Chêne","150x80x75")
table1 = Table(350,700,"TEX","Verre","Transparent","20x60x75")
