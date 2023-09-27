# Crée par Maximilien Cloutier
# Crée en 2023
# Code du TP2

# Importation de random
import random

# Variables globales
nombreEssais = 0
essai = -1
reponse = True
inconnu = random.randint(0, 1000)
hs = -1

# Boucles qui va éxecuter la question jusqu'à ce que le nombre est trouvé
while (reponse):
    essai = int(input("Entrez un chiffre de 0 à 1000 :"))

    nombreEssais += 1

    # Tant que le nombre n'est pas trouvé
    if essai != inconnu:

        # Si le nombre est plus grand que le nombre recherché
        if essai > inconnu:
            print("Le nombre recherché est plus petit que", essai)

        # Si le nombre est plus petit que le nombre recherché
        elif essai < inconnu:
            print("Le nombre recherché est plus grand que", essai,)

    # Si le nombre recherché est trouvé
    elif essai == inconnu:
        print("\n\nBravo! Le nombre recherché était", inconnu, "\nVotre score est : %d" % (nombreEssais))
        reponse = False