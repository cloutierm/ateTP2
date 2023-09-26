# Crée par Maximilien Cloutier
# Crée en 2022
# Exercice de raffraichissement

# Importation de random
import random

# Variables globales
nombreEssais = 0
essai = -1
reponse = True
inconnu = random.randint(0, 100)
hs = -1

while (reponse):
    essai = int(input("Entrez un chiffre de 0 à 100 :"))

    nombreEssais += 1

    if essai != inconnu:

        print("Mauvaise réponse, vous avez essayé %d fois \n" % (nombreEssais))

        if essai > inconnu:
            print("Votre nombre est trop grand.")

        else:
            print("Votre nombre est trop petit.")

    elif essai:
        print("\n\nBravo!Votre score est : %d" % (nombreEssais))