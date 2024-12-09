import random

#test de la classe


class Voiture:
    numero_serie = 1  # Numéro de série global pour toutes les voitures

    def __init__(self, marque, modele, prix, couleur):
        self.marque = marque
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.numero = (
            Voiture.numero_serie
        )  # Attribuer un numéro de série unique à chaque voiture
        Voiture.numero_serie += (
            1  # Incrémenter le numéro de série pour la prochaine voiture
        )

    def changer_couleur(self, nouvelle_couleur):
        """Changer la couleur de la voiture."""
        self.couleur = nouvelle_couleur

    def remise_de_prix(self):
        """Appliquer une remise au prix de la voiture si demandé par l'utilisateur."""
        demande_prix = (
            input(
                f"Voulez-vous appliquer une remise sur la voiture {self.marque} {self.modele} ? (oui ou non) : "
            )
            .strip()
            .lower()
        )

        if demande_prix == "oui":
            # Appliquer une remise de 50%
            self.prix /= 2
            print(
                f"Le prix de la voiture {self.marque} {self.modele} a été réduit à {self.prix} euros."
            )
        elif demande_prix == "non":
            print("Pas de remise appliquée.")
        else:
            print("Entrée non reconnue, aucune modification effectuée.")

    def afficher_details(self):
        """Afficher les détails de la voiture."""
        print(
            f"Voiture {self.numero}: {self.marque} {self.modele}, {self.couleur}, Prix: {self.prix}€"
        )

#test de la classe
