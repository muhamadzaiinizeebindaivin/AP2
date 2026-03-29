import graphviz

def generation_png(arbre, nom_fichier="arbre"):
    if arbre.racine is None:
        print("Arbre vide")
        return
    dot = graphviz.Digraph(comment="ARBRE")
    
    def parcourir(noeud):
        if noeud is None:
            return
        dot.node(str(id(noeud)), str(noeud.valeur))
        fils_gauche = noeud.fils[0]
        fils_droit = noeud.fils[1]
        if fils_gauche is not None:
            dot.edge(str(id(noeud)), str(id(fils_gauche)))
            parcourir(fils_gauche)
        if fils_droit is not None:
            dot.edge(str(id(noeud)), str(id(fils_droit)))
            parcourir(fils_droit)
    
    parcourir(arbre.racine)
    dot.render("img/"+nom_fichier, format='png', cleanup=True)
    print(f"Sauvegardé : {nom_fichier}.png")