import graphviz
import subprocess

def ajouter_noeud(dot, id, compteur):
    dot.node(id, str(compteur))

def ajouter_edge(dot, id1, id2):
    dot.edge(id1, id2)
    
def visualiser_plateaux(plateau, s):
    dot = graphviz.Digraph(comment="Plateaux atteignables")
    compteur_noeuds = 0  # un compteur pour des indentifiants uniques

    def parcourir(plateau, profondeur, id_pere):
        nonlocal compteur_noeuds
        if profondeur == 0:
            return
        for coup in plateau.coups():
            fils = plateau.joue_coup(coup)
            compteur_noeuds += 1
            id_fils = str(compteur_noeuds)
            ajouter_noeud(dot, id_fils, fils.compteur)
            ajouter_edge(dot, id_pere, id_fils)
            parcourir(fils, profondeur - 1, id_fils)

    # Add root node
    root_id = "0"
    ajouter_noeud(dot, root_id, plateau.compteur)
    parcourir(plateau, s, root_id)

    # afficher avec kitty
    png_data = dot.pipe(format='png')
    subprocess.run(['kitty', '+kitten', 'icat', '--stdin', 'yes'], input=png_data)