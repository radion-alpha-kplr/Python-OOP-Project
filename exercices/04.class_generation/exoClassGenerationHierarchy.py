import json
import re
from unidecode import unidecode
import os

# on commence par 1)chargé le fichier json 
# #2)le convertir en chaine de caractère
# 3)fonction unidecode pour enlever les accents et autres caractères spéciaux
# 4)Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python

# 1)
local_path = os.path.dirname(os.path.abspath(__file__))
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
# 2)
json_str = json.dumps(json_data)
# 3)
json_data = (unidecode(json_str))
# 4)
json_dict = json.loads(json_data)

def generate_class_def(nom_classe: str, attributs: dict, nom_superclasse: str, args_superclasse: list = []) -> str:
    args_constructeur = [] # une liste qui stocke les noms des attributs qui seront utilisés pour créer le constructeur
    definition_constructeur = "" # une chaîne de caractères qui stocke le code qui sera utilisé pour initialiser les attributs de la classe
    has_attributs = False # un booléen qui vérifie si la classe a des attributs ou non
    modele_classe = f"class {nom_classe}" # une chaîne de caractères qui stocke la définition de base de la classe
    if nom_superclasse: # si la classe a une superclasse
        modele_classe += f"({nom_superclasse})" # ajouter la superclasse à la définition de la classe
        modele_classe += ":\n" # ajouter une nouvelle ligne à la définition de la classe
        for nom_attribut in attributs.keys(): # pour chaque attribut dans le dictionnaire d'attributs
            if nom_attribut != "subclasses": # si l'attribut n'est pas une sous-classe
                has_attributs = True # la classe a des attributs
                args_constructeur.append(nom_attribut) # ajouter le nom de l'attribut à la liste des arguments du constructeur
                definition_constructeur += f"\n\t\tself.{nom_attribut} = {nom_attribut}" # ajouter une ligne au code de définition du constructeur pour initialiser l'attribut
    if nom_classe == "Product": # si la classe est de type Product
        definition_constructeur += "\n\t\tself.name=type(self).__name__" # ajouter une ligne au code de définition du constructeur pour initialiser le nom de la classe
    if has_attributs: # la classe a des attributs
        modele_constructeur = f"\tdef __init__(self, {', '.join(args_constructeur + args_superclasse)}):" # créer la signature du constructeur en incluant les arguments des attributs et les arguments de la superclasse

        if len(args_superclasse) > 0: # si la superclasse a des arguments
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})" # ajouter une ligne pour initialiser la superclasse

        modele_constructeur += definition_constructeur # ajouter le code d'initialisation des attributs à la définition du constructeur
    else: # la classe n'a pas d'attributs
        if len(args_superclasse) > 0: # si la superclasse a des arguments
            modele_constructeur = f"\tdef __init__(self, {', '.join(args_superclasse)}):" # créer la signature du constructeur en incluant les arguments de la superclasse
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})"
      
        else:    
            modele_constructeur = "\tpass"

    return modele_classe + modele_constructeur + "\n\n"
          


def generate_class_hierarchy(json_dict :dict, superclass_name:str=None,superclass_args:list=[]):
    # Initialisation de la chaîne de caractères contenant les définitions de classes
    class_defs = ""
    for class_name,class_attrs in json_dict.items():    
#le résultat de la méthode generate_class_def() est stocker dans une variable 'class_def'
        class_def = generate_class_def(class_name,class_attrs,superclass_name,superclass_args)
#Concaténer la définition de la classe à la chaîne de caractères class_defs
        class_defs = class_defs+class_def

#Ensuite, vérifier la présence des sous-classes dans la classe courante
#Si "subclasses" existe parmi les attributs de la classe courante, faire:
#    -Construire une liste "super_attr" contenant les attributs de la classe courante concaténées aux arguments de la superclasse
#    -Puis, supprimer l'attribut 'subclasses' à partir de la liste créée
    if "subclasses" in class_attrs:
        super_attrs = (list(class_attrs.keys())+superclass_args)
        super_attrs.remove("subclasses")
# Ensuite, faire une récursion pour générer la définition de la sous-classe en utilisant la méthode generate_class_hierarchy
# En passant le nom de la classe courante en tant que superclass_name et la liste super_attr en tant que superclass_args
# Concaténer la définition de la sous-classe à la chaîne de caractères class_defs   
        #for class_name,class_attrs in json_dict.items() : 
        subclass_defs = generate_class_hierarchy(class_attrs("subclasses"), superclass_name,super_attrs)
        class_defs += subclass_defs
# Retourne la chaîne de caractères contenant les définitions de classes    
    return class_defs


def write_content(content,filename):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)
        

# Appeler la méthode generate_class_hierarchy pour générer le code des classes automatiquement en se basant sur le dictionnaire json_dict
# Stocker le résultat de la classe dans une variable
# Appeler la fonction write_content pour stocker le code des classes dans un fichier Python 'product_classes.py'


content = generate_class_hierarchy(json_dict)

write_content(content,'product_classes.py')
