from arbre import Arbre
from noeud import Noeud
from visualisation import *
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
    
    
def arbre_enorme():
    a7 = Arbre()
    a7.racine = Noeud(50,
    Noeud(25,
        Noeud(12,
            Noeud(6,
                Noeud(3),
                Noeud(9)),
            Noeud(18,
                Noeud(15),
                Noeud(21))),
        Noeud(37,
            Noeud(31,
                Noeud(28),
                Noeud(34)),
            Noeud(43,
                Noeud(40),
                Noeud(46)))),
    Noeud(75,
        Noeud(62,
            Noeud(56,
                Noeud(53),
                Noeud(59)),
            Noeud(68,
                Noeud(65),
                Noeud(71))),
        Noeud(87,
            Noeud(81,
                Noeud(78),
                Noeud(84)),
            Noeud(93,
                Noeud(90),
                Noeud(96)))))
    return a7

if __name__ == "__main__":
    # generer_png()
    # abre_sans_racine = Arbre()
    # print("abre_sans_racine.delete(6) : ", abre_sans_racine.delete(6))
    # # print(abre_sans_racine.verif())
    # visualiser(abre_sans_racine)
    
    # arbre_juste_racine = Arbre()
    # arbre_juste_racine.racine = Noeud(1)
    # # print(arbre_juste_racine.verif())
    # visualiser(arbre_juste_racine)
    # print("arbre_juste_racine.delete(1) : ", arbre_juste_racine.delete(1))
    # visualiser(arbre_juste_racine)

    
    a1 = Arbre()
    a1.racine = Noeud(5, Noeud(3), Noeud(7))
    # visualiser(a1)
    # a1.delete(5)
    # visualiser(a1)
    # a1.delete(5)
    # visualiser(a1)
    # print("verif arbre a1 : ", a1.verif())
    
    # a2 = Arbre()
    # a2.racine = Noeud(1, None, Noeud(3, None, Noeud(6)))
    # print("verif arbre a2 : ", a2.verif())
    
    # a3 = Arbre()
    # a3.racine = Noeud(5, Noeud(7), Noeud(8))
    # print("verif arbre a3 : ", a3.verif())
    
    a4 = Arbre()
    a4.racine = Noeud(10, Noeud(5, Noeud(2), Noeud(7)), Noeud(15))
    print("verif arbre a4 : ", a4.verif())
    visualiser(a4)
    a4.delete(10)
    visualiser(a4)
    # a5 = Arbre()
    # a5.racine = Noeud(200, Noeud(29, Noeud(6), Noeud(201)), Noeud(203))
    # print("verif arbre particulier : ", a5.verif())
    # generation_png(a5, "arbre_5")
    
    # a6 = Arbre()
    # a6.racine = Noeud(6, Noeud(3, Noeud(1)))
    # print("verif arbre a6 : ", a6.verif())
    # generation_png(a6, "arbre_6")
    # a7 = arbre_enorme()
    # a7.delete(25)
    # print(a7.verif())