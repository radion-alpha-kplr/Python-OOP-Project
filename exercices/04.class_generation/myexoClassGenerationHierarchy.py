import json
import re
from unidecode import unidecode
import os
import exo02class_generation

def trimspaces(data):
    # Define a regular expression pattern to match quoted substrings
    pattern = r'"[^"]*"'
    # Replace spaces and hyphens with underscore
    #return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), str(unidecode(json.dumps(data))))
    data_s=json.dumps(data)
    return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), data_s)
# on commence par 1)chargé le fichier json 
# #2)le convertir en chaine de caractère
# 3)fonction unidecode pour enlever les accents et autres caractères spéciaux
# 4)Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python

# 1)
local_path = os.path.dirname(os.path.abspath(__file__))
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
# 2)
json_str = trimspaces(json_data)
#json_str = json.dumps(json_data)
# 3)
json_data = unidecode(json_str)

# 4)
json_dict = json.loads(json_data)
  


def generate_class_hierarchy(json_dict :dict, superclass_name:str=None,superclass_args:list=[]):
    # Initialisation de la chaîne de caractères contenant les définitions de classes
    class_defs = ""
    for class_name,class_attrs in json_dict.items() :    
#le résultat de la méthode generate_class_def() est stocker dans une variable 'class_def'
        class_def = exo02class_generation.generate_class_def(class_name,class_attrs,superclass_name,superclass_args)
#Concaténer la définition de la classe à la chaîne de caractères class_defs
        class_defs += class_def

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
            subclass_defs = generate_class_hierarchy(class_attrs["subclasses"], class_name,super_attrs)
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
