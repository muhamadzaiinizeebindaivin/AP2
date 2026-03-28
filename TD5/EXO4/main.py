from arbre import *
from noeud import * 
from visualisation import *

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

if __name__=="__main__":
    a1 = arbre_enorme()
    visualiser(a1)
    a1.iterate(5, 24)
    
    # a4 = Arbre()
    # a4.racine = Noeud(10, Noeud(5, Noeud(2), Noeud(7)), Noeud(15))
    # visualiser(a4)
    # a4.iterate(2, 8)