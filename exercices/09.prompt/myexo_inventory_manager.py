#La classe "InventoryManager" est une classe qui permet de gérer un inventaire de produits. 

from typing import Dict
from myexo_inventory_product_entry import InventoryProductEntry
from product_classes import Product



class InventoryManager:
    # Initialisation de la classe
    def __init__(self):
        # Vous initialisez un dictionnaire 'inventory' qui stocke l'inventaire de tous les produits
        # Il prend comme clé le nom du produit, et la valeur est un objet InventoryProductEntry
        self.inventory : Dict[str, InventoryProductEntry] = {}

    #Méthode product_exists
    """"
    La fonction prend un objet Product en entrée et vérifie si son nom est une clé dans le dictionnaire self.inventory. 
    Si c'est le cas, la fonction retourne True, sinon elle retourne False.
    """
    def product_exists(self,product:Product):
        for clefs in self.inventory : 
            if (clefs == product.name):
                return True 
        return False
        
        """
        pour chaque 'inventory_product_entry_key' dans self.inventory faire:
            si 'inventory_product_entry_key' est égal à product.name alors:
                retourner True
        retourner False
        """
    
#Méthode add_product
    """
    La méthode add_product est utilisée pour ajouter un nouveau produit à l'inventaire.
    Elle prend en argument un objet Product et une quantité initiale.
    """
    def add_product(self, product:Product, quantity):
        if self.product_exists in self.inventory :
            print("ce produit existe déjà dans l'inventaire")
        else :
            inventory_product_entry = InventoryProductEntry(product, quantity)
            self.inventory[product.name]=inventory_product_entry
   
   
        """
        SI le produit existe déjà dans l'inventaire: 
            afficher un message pour informer l'utilisateur
        Sinon:
            Créer un nouvel objet InventoryProductEntry en utilisant le produit et la quantité fournis
            Ajouter le nouvel objet au dictionnaire 'inventory'
        """
    
    #Méthode remove_product
    """
    La méthode remove_product est utilisée pour supprimer un produit de l'inventaire.
    Elle prend en argument un nom de produit et supprime l'entrée correspondante dans le dictionnaire 'inventory'.
    """
    def remove_product(self, product:Product):
        if self.product_exists(self,product) :
            self.inventory.pop(product.name)
        else :
            print("le produit n'a pas été trouvé")
        #Utiliser la méthode product_exists pour vérifier si le produit existe dans l'inventaire
        #Si le produit est trouvé, supprimer le de l'inventaire
        #Sinon, afficher un message d'erreur indiquant que le produit n'a pas été trouvé
    
    #Méthode sell_product
    """
    La méthode sell_product est utilisée pour vendre une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à vendre.
    """
    
    def sell_product(self, product:Product, quantity):
        for clefs in self.inventory :
            if clefs  == product.name:
                InventoryProductEntry.sell(self, quantity)
            else :
                print("le produit n'est pas en stock la vente à échoué")
        #Utiliser une boucle pour parcourir les clés du dictionnaire 'inventory'
        #Pour chaque itération, on vérifie si le nom du produit fourni est équal à la clé du dictionnaire.
        #Si le produit est trouvé, appeler la méthode 'sell' de l'objet InventoryProductEntry correspondant avec la quantité à vendre
        #Sinon, afficher un message d'erreur indiquant que la vente a échoué
    
    #Méthode restock_product
    """
    La méthode restock_product est utilisée pour restocker une quantité donnée d'un produit.
    Elle prend en argument le nom du produit et la quantité à restocker.
    """
    def restock_product(self, product:Product, quantity):
        if self.product_exists(product):
            self.inventory[product.name].restock(quantity)
        else :
            self.add_product(product, 0)
            self.restock_product(product,quantity)

        #Vérifier si le produit existe déjà dans l'inventaire
        #Si le produit est trouvé, appeler la méthode 'restock' de l'objet InventoryProductEntry correspondant avec la quantité à restocker
        #Si le réapprovisionnement est réussi, afficher un message de confirmation
        #Sinon, on appelle la méthode add_product pour ajouter le produit en stock avec une quantité nulle et on rappelle la fonction restock_product pour le restocker
    
    
    #Méthode get_product
    """
    La méthode get_product retourne toutes les informations liées au produit en faisant une recherche par son nom.
    Elle prend en entrée un nom de produit.
    """
    def get_product(self, name):
        for clef in self.inventory.items() :
            if clef == name:
                return self.inventory[clef].product 
            print("le produit",name," n'existe pas")
            

    """
            pour chaque inventory_product_entry_key dans self.inventory:
                si inventory_product_entry_key == nom de produit:
                    retourner self.inventaire[inventory_product_entry_key].product
            afficher un message pour indiquer que le produit n'existe pas
    """

        #Méthode list_products
    """
            La méthode list_products(self) parcourt tous les produits de l'inventaire 
            et affiche les informations relatives à chacun d'entre eux (nom, quantité disponible, prix unitaire, coût unitaire, prix de vente unitaire, bénéfice unitaire). 
    """
    def list_products(self):
        for clefs in self.inventory :
            print(self.inventory[clefs])
        return self.inventory        
