import random


class Voiture:
    numero_serie = 0  # Numéro de série global pour toutes les voitures

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


# Liste de marques et modèles pour la simulation
marques = [
    "Toyota",
    "Peugeot",
    "Renault",
    "Ford",
    "Volkswagen",
    "BMW",
    "Audi",
    "Mercedes",
    "Honda",
    "Nissan",
]
modeles = [
    "Clio",
    "Golf",
    "Corolla",
    "Focus",
    "208",
    "Passat",
    "A3",
    "Civic",
    "Altima",
    "Accord",
]
couleurs = [
    "rouge",
    "bleu",
    "noir",
    "blanc",
    "gris",
    "vert",
    "jaune",
    "orange",
    "argent",
    "marron",
]


# Fonction pour générer un prix aléatoire entre 10 000 et 50 000 €
def generer_prix():
    return random.randint(10000, 50000)


# Création de 100 voitures avec des caractéristiques aléatoires
voitures = []
for _ in range(100):
    marque = random.choice(marques)
    modele = random.choice(modeles)
    prix = generer_prix()
    couleur = random.choice(couleurs)
    voiture = Voiture(marque, modele, prix, couleur)
    voitures.append(voiture)

# Affichage des 10 premières voitures créées
print("Affichage des 10 premières voitures créées :\n")
for voiture in voitures[:10]:
    voiture.afficher_details()

# Simulation d'application de remises
print("\nAppliquer une remise à quelques voitures sélectionnées...")
for voiture in voitures[:5]:
    voiture.remise_de_prix()  # Demande de remise pour les 5 premières voitures

# Affichage des détails des voitures après modification (si remise appliquée)
print("\nAffichage des 10 premières voitures après modification :")
for voiture in voitures[:10]:
    voiture.afficher_details()

# Modification aléatoire de la couleur pour certaines voitures
print("\nChangement de couleur pour certaines voitures...")
for voiture in voitures[:5]:
    nouvelle_couleur = random.choice(couleurs)
    voiture.changer_couleur(nouvelle_couleur)
    print(f"Voiture {voiture.numero} changée en {nouvelle_couleur}.")

# Affichage final des voitures avec changement de couleur
print("\nAffichage final des 10 premières voitures :")
for voiture in voitures[:10]:
    voiture.afficher_details()
