from arbre import Arbre
from noeud import Noeud
from import_png import *

def generer_abr():
    # 1. ABR simple (3 noeuds)
    #       5
    #      / \
    #     3   7
    a1 = Arbre()
    a1.racine = Noeud(5, Noeud(3), Noeud(7))

    # 2. ABR filiforme (que des fils droits)
    #   1
    #    \
    #     3
    #      \
    #       6
    a2 = Arbre()
    a2.racine = Noeud(1, None, Noeud(3, None, Noeud(6)))

    # 3. PAS un ABR (7 à gauche de 5, invalide)
    #       5
    #      / \
    #     7   8
    a3 = Arbre()
    a3.racine = Noeud(5, Noeud(7), Noeud(8))

    # 4. ABR plus grand
    #         10
    #        /  \
    #       5    15
    #      / \
    #     2   7
    a4 = Arbre()
    a4.racine = Noeud(10, Noeud(5, Noeud(2), Noeud(7)), Noeud(15))
    
    return [a1, a2, a3, a4]

def generer_png():
    for i, a in enumerate(generer_abr()):
        generation_png(a, f"img/arbre_{i+1}")
        

if __name__ == "__main__":
    # generer_png()
    # abre_sans_racine = Arbre()
    # print(abre_sans_racine.verif())
    
    # arbre_juste_racine = Arbre()
    # arbre_juste_racine.racine = Noeud(1)
    # print(arbre_juste_racine.verif())
    
    a1 = Arbre()
    a1.racine = Noeud(5, Noeud(3), Noeud(7))
    print("verif arbre a1 : ", a1.verif())
    
    a2 = Arbre()
    a2.racine = Noeud(1, None, Noeud(3, None, Noeud(6)))
    print("verif arbre a2 : ", a2.verif())
    
    a3 = Arbre()
    a3.racine = Noeud(5, Noeud(7), Noeud(8))
    print("verif arbre a3 : ", a3.verif())
    
    a4 = Arbre()
    a4.racine = Noeud(10, Noeud(5, Noeud(2), Noeud(7)), Noeud(15))
    print("verif arbre a4 : ", a4.verif())
    
    a5 = Arbre()
    a5.racine = Noeud(200, Noeud(29, Noeud(6), Noeud(201)), Noeud(203))
    print("verif arbre particulier : ", a5.verif())
    generation_png(a5, "arbre_5")
    
    a6 = Arbre()
    a6.racine = Noeud(6, Noeud(3, Noeud(1)))
    print("verif arbre a6 : ", a6.verif())
    generation_png(a6, "arbre_6")
