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
    
    def verif(self):
        if self.racine is None:
            return (True, 0, 0)
        return self.racine.verif()
    
    def delete(self, key):
        if self.racine is None:
            return False
        self.racine = self.racine.delete(key)