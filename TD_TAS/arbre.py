class Arbre:
    def __init__(self, racine=None):
        self.racine = racine
    
    def pere(self, i):
        return self.racine.pere(i)