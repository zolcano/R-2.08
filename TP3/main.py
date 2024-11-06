from Class import *
import json
from datetime import datetime

# Créer une instance de Bibliotheque
ma_bibliotheque = Bibliotheque()

Planete = Film(titre="Planete", sortie="02/03/1904", note=3.2)
Planete.addavis("j'ai bien aimé")
Planete.addavis("j'ai pas aimé")
ma_bibliotheque.ajouter_film(Planete)  # Utiliser l'instance de Bibliotheque

Gladiator = Film(titre="Gladiator", sortie="05/05/2000", note=4.5)
Gladiator.addavis("Epix historical drama!")
Gladiator.addavis("Russell Crowe delivers a powerhouse performance!")
ma_bibliotheque.ajouter_film(Gladiator)  # Utiliser l'instance de Bibliotheque

print(Planete)
print(Gladiator)

print("\n\n")

ma_bibliotheque.afficher_films()  # Utiliser l'instance de Bibliotheque
