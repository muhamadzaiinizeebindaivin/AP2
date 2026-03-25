class Arbre:
    def __init__(self):
        self.racine = None
    
    def mirroir_fonctionnelle(self):
        if self.racine is None:
            return Arbre()
        racine = self.racine.mirroir_fonctionnelle_noeud()
        nouveau_arbre = Arbre()
        nouveau_arbre.racine = racine
        return nouveau_arbre
        
    def mirroir_procedurale(self):
        if self.racine is None:
            return self
        self.racine.miroir_procedurale_noeud()