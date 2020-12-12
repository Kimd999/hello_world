class Card : 


    """classe servant à créer une carte : 
    Elle sera définie par sa couleur et sa valeur. 
    Pour les couleurs et les valeurs, on crée deux listes"""

    couleur = ['trèfle', 'dame', 'coeur', 'pique']
    valeur = ['As', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']

    def _init_(self) :

        "constructeur par défaut d'une carte"
        self.couleur = 0
        self.valeur = 12

Roi_de_trèfle = Card()
print(Roi_de_trèfle)     

