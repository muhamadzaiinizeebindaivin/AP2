class Noeud:
    def __init__(self, valeur, fils_gauche=None, fils_droite=None):
        self.valeur = valeur
        self.fils = [fils_gauche, fils_droite]
