from arbre import *
from noeud import *

def tas_en_arbre_recursive(tas):
    def creer_arbre(i):
        if i >= len(tas):
            return None
    
        noeud = Noeud(tas[i])

        if 2*i + 1 < len(tas):
            noeud.fils[0] = creer_arbre(2*i + 1)
        
        if 2*i + 2 < len(tas):
            noeud.fils[1] = creer_arbre(2*i + 2) 
        
        return noeud
    arbre = Arbre()
    arbre.racine = creer_arbre(0)
    return arbre
        
def tas_en_abr_iterative_simple(tas):
    taille_tas = len(tas)
    if taille_tas == 0:
        return Arbre()
    noeuds = [Noeud(v) for v in tas]
    
    abr = Arbre()
    for i, noeud in enumerate(noeuds):
        if i == 0:
            abr.racine = noeud
        pere = noeud
        if 2*i + 1 <= taille_tas - 1:
            pere.fils[0] = noeuds[2*i + 1]
        if 2*i + 2 <= taille_tas - 1:
            pere.fils[1] = noeuds[2*i + 2]
    return abr