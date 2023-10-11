# Crée par Maximilien Cloutier
# Crée en 2023
# Code du TP2

import random

def jeu(): # Fonction qui va executer tout le code du jeu

    rejouer = True

    # Boucle qui va executer le jeu et si la personne veurt rejouer, la boucle va recommencer
    while (rejouer):


        nombreEssais = 0
        reponse = True

        nbr1 = int(input("Entrer le premier notre de votre intervale: "))
        nbr2 = int(input("Entrer le deuxième nombre de votre intervale: "))

        inconnu = random.randint(nbr1, nbr2)

        # Boucles qui va éxecuter la question jusqu'à ce que le nombre est trouvé
        while (reponse):
            essai = int(input("Entrez un chiffre de %d et %d: " % (nbr1, nbr2)))

            nombreEssais += 1

            if essai > inconnu:
                print("Le nombre recherché est plus petit que", essai)

            elif essai < inconnu:
                print("Le nombre recherché est plus grand que", essai,)

            # Si le nombre recherché est trouvé, on pose la question si elle veut recommencer ou non
            elif essai == inconnu:
                print("\n\nBravo! Le nombre recherché était", inconnu, "\nVotre score est : %d" % (nombreEssais))
                reponse = False
                # On pose la question si elle veut rejouer ou non
                repeter = str(input("Voulez-vous rejouer? "))
                if repeter == "oui":
                    rejouer = True

                elif repeter == "non":
                    rejouer = False
                    print("Bye")

                else:
                    print("Je n'ai pas compris, bye.")
                    rejouer = False