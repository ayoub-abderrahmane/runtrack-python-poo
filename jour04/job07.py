import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def calculer_points(self, main):
        total_points = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ['J', 'Q', 'K']:
                total_points += 10
            elif carte.valeur == 'A':
                as_count += 1
            else:
                total_points += int(carte.valeur)

        for _ in range(as_count):
            if total_points + 11 <= 21:
                total_points += 11
            else:
                total_points += 1

        return total_points

    def afficher_main(self, main):
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def jouer_partie(self):
        joueur_main = [self.paquet.pop(), self.paquet.pop()]
        croupier_main = [self.paquet.pop(), self.paquet.pop()]

        while True:
            print("Main du joueur:")
            self.afficher_main(joueur_main)
            choix = input("Voulez-vous prendre une carte supplémentaire ? (Oui/Non): ").lower()

            if choix == 'oui':
                joueur_main.append(self.paquet.pop())
                points_joueur = self.calculer_points(joueur_main)

                if points_joueur > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    return
            else:
                break

        while self.calculer_points(croupier_main) < 17:
            croupier_main.append(self.paquet.pop())

        print("\nMain du joueur:")
        self.afficher_main(joueur_main)
        print(f"Total des points du joueur: {self.calculer_points(joueur_main)}\n")

        print("Main du croupier:")
        self.afficher_main(croupier_main)
        print(f"Total des points du croupier: {self.calculer_points(croupier_main)}\n")

        points_joueur = self.calculer_points(joueur_main)
        points_croupier = self.calculer_points(croupier_main)

        if points_joueur > 21 or (points_croupier <= 21 and points_croupier >= points_joueur):
            print("Le croupier gagne.")
        else:
            print("Le joueur gagne.")

jeu = Jeu()
jeu.jouer_partie()