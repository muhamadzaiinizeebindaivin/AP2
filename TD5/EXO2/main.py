from plateau import *
from visualisation import *

def petit_test():
    p1 = Plateau(3)
    p2 = Plateau(3)
    
    print(p1 == p2)
    print(p1 in {p2})

if __name__ == "__main__":
    plateau = Plateau()
    visualiser_plateaux(plateau, 5)
    # print(plateau.coups())
    print("compter_plateaux_recursive")
    print(compter_plateaux_recursive(plateau, 2))
    print(compter_plateaux_recursive(plateau, 4))

    print()
    print("compter_plateaux_iterrative")
    print(compter_plateaux_iterative(plateau, 2))
    print(compter_plateaux_iterative(plateau, 4))
    
    # for p in iterateur_plateau(plateau, 2):
    #     visualiser_plateaux(p, 2)
    
    print()
    print("compter_plateaux_avec_iterateur")
    print(compter_plateaux_avec_iterateur(plateau, 2))
    print(compter_plateaux_avec_iterateur(plateau, 4))
    
    print()
    print("iterateur_plateau_sans_doublons_dfs")
    print(compter_plateaux_avec_iterateur_sans_doublons_dfs(plateau, 2))
    print(compter_plateaux_avec_iterateur_sans_doublons_dfs(plateau, 4))
    
    # petit_test()
    
    print()
    print("iterateur_plateau_sans_doublons_bfs")
    print(compter_plateaux_avec_iterateur_sans_doublons_bfs(plateau, 2))
    print(compter_plateaux_avec_iterateur_sans_doublons_bfs(plateau, 4))
    