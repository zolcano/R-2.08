from voiture import *

mycar1 = Voiture()
mycar2 = Voiture(marque='toyota', modele='corolla', puissance_fiscale='5', couleur='jaune')
mycar2.ajouter_option('clim')

mycar1.set_marque("toyota")
mycar1.set_modele("corolla")
mycar1.set_puissance_fiscale('5')
mycar1.set_couleur("jaune")

print(mycar1)
print(mycar2)

mycar2.supprimer_option('clim')

print(mycar2)