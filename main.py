# importation des librairie
import os
from functions import *

# debut du code
start_code = True
while start_code:
    print("GESTION DES NOTES")

    choice = input("choisissez un menu s'il vous plait\n"
        "Entrer:\n"
          "C pour créer une classe\n"
          "A pour inscrire un etudiant\n"
          "S pour saisir les notes d'un etudiant\n"
          "N pour afficher les notes d'un etudiant\n"
          "M pour afficher la moyenne d'un etudiant\n"
          "appuyer sur une autre touche pour quitter\n")

    if choice == "C" or choice == "c":
        create()
    elif choice == "A" or choice == "a":
        register()
    elif choice == "S" or choice == "s":
        input_note()
    elif choice == "N" or choice == "n":
        print_note()
    elif choice == "M" or choice == "m":
        print_average()
    else:
        stop_code = input("voulez vous quitter le programme (o,n)")
        if stop_code == ("o") or stop_code == ("O") :
            start_code = False

# fin du code
os.system("pause")
