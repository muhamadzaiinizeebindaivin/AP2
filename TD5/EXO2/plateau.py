class Plateau:
    def __init__(self, compteur=0):
        self.compteur = compteur
        
    def coups(self):
        if self.compteur >= 5:
            return []
        return [1, 2]
    
    def joue_coup(self, coup):
        return Plateau(self.compteur + coup)
    

def compter_plateaux_recursive(plateau, s):
    if s == 0:
        return 1
    cpt = 0
    for coup in plateau.coups():
        cpt += compter_plateaux_recursive(plateau.joue_coup(coup), s-1)
    return cpt

def compter_plateaux_iterative(plateau, s):
    if s == 0:
        return 1
    cpt = 0
    coups_a_appliquer = []
    while s > 0:
        cpt += len(plateau.coups())
        coups_a_appliquer.extend(plateau.coups())
        plateau = plateau.joue_coup(coups_a_appliquer.pop())
        s -= 1
    return cpt