# Crée par Maximilien Cloutier
# Crée en 2023
# Code du TP2


rejouer = True


while (rejouer):

    # Importation de random
    import random

    # Variables globales
    nombreEssais = 0
    essai = -1
    reponse = True

    # Choix des l'intervale
    nbr1 = int(input("Entrer le premier notre de votre intervale: "))
    nbr2 = int(input("Entrer le deuxième nombre de votre intervale: "))

    # Choix du nombre aleatoire
    inconnu = random.randint(nbr1, nbr2)

    # Boucles qui va éxecuter la question jusqu'à ce que le nombre est trouvé
    while (reponse):
        essai = int(input("Entrez un chiffre de %d et %d: " % (nbr1, nbr2)))

        nombreEssais += 1

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
            repeter = str(input("Voulez-vous rejouer? "))
            if repeter == "oui": # Si la personne veut rejouer
                rejouer = True

            elif repeter == "non": # Si la personne ne veut pas rejouer
                rejouer = False
                print("Bye")

            else:
                print("Je n'ai pas compris, bye.")
                rejouer = False