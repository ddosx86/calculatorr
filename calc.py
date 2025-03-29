print("Welcome to calculatorr v0.1 ")
from colorama import Fore, Style

# Lire le fichier contenant le logo
with open("logo.txt", "r") as file:
        logo = file.read()
# Lire le fichier contenant le help
with open("help.txt", "r") as file:
            h = file.read()

# Afficher en vert hacker
print(Fore.GREEN + logo + Style.RESET_ALL)
# affiche la base
print("Entrez une opération ou 'exit' pour quitter et h pour la liste des commande  ")
while True:
    #demander l'operation
    user_input = input("calc:</ ")
    # Si l'utilisateur veut quitter
    if user_input == 'exit':
        print("Bye !")
        break
    elif user_input == 'h' :
        print(h)
        continue
    
    try:
        # Utilisation de eval pour calculer l'expression
        result = eval(user_input)
        print(f"Résultat : {result}")
    except Exception as e:
        print(f"Erreur.  Assurez-vous d'entrer une expression correcte")



