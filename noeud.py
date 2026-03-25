class Noeud:
    def __init__(self, valeur, fils_gauche = None, fils_droit = None):
        self.valeur = valeur
        self.fils = [fils_gauche, fils_droit]
    
    def mirroir_fonctionnelle_noeud(self):
        pere = Noeud(self.valeur)
        if self.fils[1] is not None:
            pere.fils[0] = self.fils[1].mirroir_fonctionnelle_noeud()
        if self.fils[0] is not None:
            pere.fils[1] = self.fils[0].mirroir_fonctionnelle_noeud()
        return pere
            

    def miroir_procedurale_noeud(self):
        fils_gauche = self.fils[0]
        fils_droit = self.fils[1]
        
        self.fils[0], self.fils[1] = fils_droit, fils_gauche
        if fils_gauche is not None:
            fils_gauche.miroir_procedurale_noeud()
        if fils_droit is not None:
            fils_droit.miroir_procedurale_noeud()
