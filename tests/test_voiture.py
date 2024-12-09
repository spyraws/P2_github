import unittest
from io import StringIO
from unittest.mock import patch
import sys
import os

# Ajouter 'src' au sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from projet_github import Voiture
from src.projet_github import Voiture  


class TestVoiture(unittest.TestCase):

    def test_initialisation_voiture(self):
        """Vérifier la création d'une voiture avec des attributs valides"""
        voiture = Voiture("Toyota", "Corolla", 20000, "rouge")
        self.assertEqual(voiture.marque, "Toyota")
        self.assertEqual(voiture.modele, "Corolla")
        self.assertEqual(voiture.prix, 20000)
        self.assertEqual(voiture.couleur, "rouge")
        self.assertEqual(voiture.numero, 101)  # Le premier numéro de série doit être 101

    @patch("builtins.input", return_value="oui")  # Simule la saisie utilisateur "oui"
    def test_remise_de_prix(self, mock_input):
        """Tester la méthode remise_de_prix pour appliquer une remise"""
        voiture = Voiture("Peugeot", "208", 15000, "bleu")
        voiture.remise_de_prix()
        self.assertEqual(voiture.prix, 7500)  # Le prix doit être divisé par 2 après remise

    def test_changer_couleur(self):
        """Tester la méthode changer_couleur pour modifier la couleur de la voiture"""
        voiture = Voiture("Renault", "Clio", 12000, "vert")
        voiture.changer_couleur("noir")
        self.assertEqual(voiture.couleur, "noir")  # La couleur doit être changée en noir

    @patch("builtins.input", return_value="non")  # Simule la saisie utilisateur "non"
    def test_remise_de_prix_pas_appliquee(self, mock_input):
        """Tester le cas où la remise n'est pas appliquée"""
        voiture = Voiture("BMW", "X5", 50000, "blanc")
        voiture.remise_de_prix()
        self.assertEqual(voiture.prix, 50000)  # Le prix doit rester inchangé

if __name__ == "__main__":
    unittest.main()
