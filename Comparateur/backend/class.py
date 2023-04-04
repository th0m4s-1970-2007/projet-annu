class PCPortable:
    def __init__(self, prix, taille_ecran, carte_graphique, ram, stockage, processeur):
        self.prix = prix
        self.taille_ecran = taille_ecran
        self.carte_graphique = carte_graphique
        self.ram = ram
        self.stockage = stockage
        self.processeur = processeur




class MSI(PCPortable):
    def __init__(self, prix, taille_ecran, carte_graphique, ram, stockage, processeur, nom_modele):
        super().__init__(3000, 16, NVIDIA RTX™ A2000 8 go GDDR6, 32 go, 1000 go, i7)
        self.nom_modele = MSI_test




class HP(PCPortable):
    def __init__(self, prix, taille_ecran, carte_graphique, ram, stockage, processeur, nom_modele):
        super().__init__(1200, 17, rtx3070 8 go, 6 go, 1000 go, i5, nom_modele)
        self.nom_modele = HP_test


