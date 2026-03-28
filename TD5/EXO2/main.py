from plateau import *
from visualisation import *

if __name__ == "__main__":
    plateau = Plateau()
    # print(plateau.coups())
    print("compter_plateaux_recursive")
    print(compter_plateaux_recursive(plateau, 0))
    print(compter_plateaux_recursive(plateau, 5))

    print()
    print("compter_plateaux_iterrative")
    print(compter_plateaux_iterative(plateau, 0))
    print(compter_plateaux_iterative(plateau, 5))

    # visualiser_plateaux(plateau, 8)