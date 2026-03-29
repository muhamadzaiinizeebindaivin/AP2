from collections import deque

class Plateau:
    def __init__(self, compteur=0):
        self.compteur = compteur
        
    def coups(self):
        if self.compteur >= 5:
            return []
        return [1, 2]
    
    def joue_coup(self, coup):
        return Plateau(self.compteur + coup)
    
    def __eq__(self, autre):
        return self.compteur == self.compteur
    
    def __hash__(self):
        return hash(self.compteur)
    

def compter_plateaux_recursive(plateau, s):
    if s == 0:
        return 1
    
    cpt = 0
    for coup in plateau.coups():
        cpt += compter_plateaux_recursive(plateau.joue_coup(coup), s-1)
    return cpt
        
def compter_plateaux_iterative(plateau, s):
    cpt = 0
    a_voir = [(plateau, s)]
    
    while a_voir:
        plateau_a_traiter, s = a_voir.pop()
        if s == 0:
            cpt += 1
        else:
            for coup in plateau_a_traiter.coups():
                a_voir.append((plateau_a_traiter.joue_coup(coup), s-1))
    return cpt

def iterateur_plateau(plateau, s):
    a_voir = [(plateau, s)]
    while a_voir:
        plateau_a_traiter, s = a_voir.pop()
        if s == 0:
            yield plateau_a_traiter
        else:
            for coup in plateau_a_traiter.coups():
                a_voir.append((plateau_a_traiter.joue_coup(coup), s-1))

def compter_plateaux_avec_iterateur(plateau, s):
    # return len(list(iterateur_plateau(plateau, s)))
    
    return sum(1 for _ in iterateur_plateau(plateau, s))

def iterateur_plateau_sans_doublons_dfs(plateau, s):
    deja_visites = {plateau}
    a_voir = [(plateau, s)]
    while a_voir:
        plateau_a_traiter, s = a_voir.pop()
        if s == 0:
            yield plateau_a_traiter
        else:
            for coup in plateau_a_traiter.coups():
                nouveau_plateau = plateau_a_traiter.joue_coup(coup)
                if nouveau_plateau not in deja_visites:
                    deja_visites.add(nouveau_plateau)
                    a_voir.append((nouveau_plateau, s-1))

def compter_plateaux_avec_iterateur_sans_doublons_dfs(plateau, s):    
    return sum(1 for _ in iterateur_plateau_sans_doublons_dfs(plateau, s))

def iterateur_plateau_sans_doublons_bfs(plateau, s):
    deja_visites = {plateau}
    a_voir = deque([(plateau, s)])
    while a_voir:
        plateau_a_traiter, s = a_voir.popleft()
        if s == 0:
            yield plateau_a_traiter
        else:
            for coup in plateau_a_traiter.coups():
                nouveau_plateau = plateau_a_traiter.joue_coup(coup)
                if nouveau_plateau not in deja_visites:
                    deja_visites.add(nouveau_plateau)
                    a_voir.append((nouveau_plateau, s-1))

def compter_plateaux_avec_iterateur_sans_doublons_bfs(plateau, s):    
    return sum(1 for _ in iterateur_plateau_sans_doublons_bfs(plateau, s))
