from visualisation import *
from tas import *

if __name__=="__main__":
    tas_vide = []
    arbre_vide = tas_en_abr_iterative_simple(tas_vide)
    visualiser(arbre_vide)
    
    tas1 = [50, 30, 40, 10, 20, 35, 25]
    # tas1_en_arbre = tas_en_abr_iterative_simple(tas1)
    # visualiser(tas1_en_arbre)
    
    tas1_en_arbre = tas_en_arbre_recursive(tas1)
    visualiser(tas1_en_arbre)