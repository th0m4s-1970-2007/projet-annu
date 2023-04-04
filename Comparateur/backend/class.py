class PCPortable:
    def __init__(self, prix, taille_ecran, carte_graphique, ram, stockage, processeur):
        self.prix = prix
        self.taille_ecran = taille_ecran
        self.carte_graphique = carte_graphique
        self.ram = ram
        self.stockage = stockage
        self.processeur = processeur

class ASUS(PCPortable):
    def __init__(self, prix, taille_ecran, carte_graphique, ram, stockage, processeur, nom_modele):
        super().__init__(prix, taille_ecran, carte_graphique, ram, stockage, processeur)
        self.nom_modele = nom_modele

class HP(PCPortable):
    def __init__(self, prix, taille_ecran, carte_graphique, ram, stockage, processeur, autonomie_batterie):
        super().__init__(prix, taille_ecran, carte_graphique, ram, stockage, processeur)
        self.autonomie_batterie = autonomie_batterie
