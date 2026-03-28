from arbre import Arbre
from noeud import Noeud
from visualisation import visualiser

def arbre1():
    racine1 = Noeud(5)
    n1 = Noeud(3)
    n2 = Noeud(7)
    n3 = Noeud(9)
    n4 = Noeud(14)
    racine1.fils = [n1, n2]
    n1.fils[0] = n3
    n2.fils[1] = n4
    arbre1 = Arbre()
    arbre1.racine = racine1
    
    return arbre1

def arbre2():
    n4 = Noeud(4)
    n5 = Noeud(5)
    n6 = Noeud(6)
    n7 = Noeud(7)
    n2 = Noeud(2, n4, n5)
    n3 = Noeud(3, n6, n7)
    n1 = Noeud(1, n2, n3)
    
    a = Arbre()
    a.racine = n1
    return a

def arbre_vide():
    return Arbre()

if __name__ == "__main__":
    a1 = arbre1()
    a2 = arbre2()
    a_vide = arbre_vide() 
    visualiser(a_vide)
    # a2.mirroir_procedurale()
    a2_mirroir_fonctionnelle = a_vide.mirroir_fonctionnelle()    
    # visualiser(a2)