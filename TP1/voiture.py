class Voiture:
        def __init__(self, marque='non specifiee', modele='non specifiee', puissance_fiscale='non specifiee', couleur='non specifiee'):
                self.__marque = marque
                self.__modele = modele
                self.__puissance_fiscale = puissance_fiscale
                self.__couleur = couleur
                self.__options = []  # Liste d'options

        # Accesseurs en lecture
        def get_options(self):
            return self.__options
        
        def get_marque(self):
            return self.__marque

        def get_modele(self):
            return self.__modele

        def get_puissance_fiscale(self):
            return self.__puissance_fiscale

        def get_couleur(self):
            return self.__couleur

        # Accesseurs en écriture

        def ajouter_option(self, option): # ajouter une option
            self.__options.append(option)

        def supprimer_option(self, option): # supprimer une option
            if option in self.__options:
                self.__options.remove(option)

        def is_option_present(self, option): # verifier option
            return option in self.__options

        def set_marque(self, nouvelle_marque):
            self.__marque = nouvelle_marque

        def set_modele(self, nouveau_modele):
            self.__modele = nouveau_modele

        def set_puissance_fiscale(self, nouvelle_puissance_fiscale):
            self.__puissance_fiscale = nouvelle_puissance_fiscale

        def set_couleur(self, nouvelle_couleur):
            self.__couleur = nouvelle_couleur

       # Affichage de l'objet
        def __str__(self):
            options_str = ', '.join(self.__options) if self.__options else "Aucune option"
            return f"-----\nVoici les caractéristiques de cette voiture:\n- Marque: {self.__marque}\n- Modèle: {self.__modele}\n- Couleur: {self.__couleur}\n- Puissance fiscale: {self.__puissance_fiscale}\n- Options: {options_str}\n-----"