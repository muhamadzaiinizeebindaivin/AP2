class Noeud:
    def __init__(self, valeur, fils_gauche = None, fils_droit = None):
        self.valeur = valeur
        self.fils = [fils_gauche, fils_droit]
    
    def mirroir_fonctionnelle_noeud(self):
        pere = Noeud(self.valeur)
        if self.fils[1] is not None:
            pere.fils[0] = self.fils[1].mirroir_fonctionnelle_noeud()
        if self.fils[0] is not None:
            pere.fils[1] = self.fils[0].mirroir_fonctionnelle_noeud()
        return pere
            
    def miroir_procedurale_noeud(self):
        fils_gauche = self.fils[0]
        fils_droit = self.fils[1]
        
        self.fils[0], self.fils[1] = fils_droit, fils_gauche
        if fils_gauche is not None:
            fils_gauche.miroir_procedurale_noeud()
        if fils_droit is not None:
            fils_droit.miroir_procedurale_noeud()
    
    def verif(self):
        if self is None:
            return (True, 0, 0)
        
        if self.fils[0] is None and self.fils[1] is None:
            return (True, self.valeur, self.valeur)
        
        if self.fils[0] is not None and self.fils[0].valeur >= self.valeur:
            return (False, 0, 0)
        
        if self.fils[1] is not None and self.fils[1].valeur <= self.valeur:
            return (False, 0, 0)
        
        est_abr_gauche, est_abr_droite = True, True
        min_gauche, max_gauche, min_droite, max_droite = 0, 0, 0, 0
        if self.fils[0] is not None:
            est_abr_gauche, min_gauche, max_gauche = self.fils[0].verif()
        if self.fils[1] is not None:
            est_abr_droite, min_droite, max_droite = self.fils[1].verif()
        
        est_abr = est_abr_gauche and est_abr_droite and (max_gauche < self.valeur) and (min_droite > self.valeur or self.fils[1] is None)
        
        min_val = self.valeur if self.fils[0] is None else min_gauche
        max_val = self.valeur if self.fils[1] is None else max_droite
            
        return (est_abr, min_val, max_val)
            
    def delete(self, key):
        if key < self.valeur:
            if self.fils[0] is not None:
                self.fils[0] = self.fils[0].delete(key)
        elif key > self.valeur:
            if self.fils[1] is not None:
                self.fils[1] = self.fils[1].delete(key)
        else:
            if self.fils[0] is None and self.fils[1] is None:
                return None
            elif self.fils[0] is None:
                return self.fils[1]
            elif self.fils[1] is None:
                return self.fils[0]
            else:
                max_gauche = self.fils[0].verif()[2]
                self.fils[0] = self.fils[0].delete(max_gauche)
                self.valeur = max_gauche
        return self

    def iterate_sans_ordre(self, min, max):
        if self.valeur >= min and self.valeur <= max:
            yield self.valeur
            if self.fils[0] is not None:
                yield from self.fils[0].iterate(min, max)
            if self.fils[1] is not None:
                yield from self.fils[1].iterate(min, max) if self.fils[1] is not None else None
        elif min > self.valeur and self.fils[1] is not None:
            yield from self.fils[1].iterate(min, max)
        elif max < self.valeur and self.fils[0] is not None:
            yield from self.fils[0].iterate(min, max)
        return
            
    # min = 2, max = 8
    def iterate(self, min, max):
        if max < self.valeur:
            if self.fils[0] is not None:
                yield from self.fils[0].iterate(min, max)
        elif min > self.valeur:
            if self.fils[1] is not None:
                yield from self.fils[1].iterate(min, max)
        elif self.valeur >= min and self.valeur <= max:
            if self.fils[0] is not None:
                yield from self.fils[0].iterate(min, max)
            yield self.valeur
            if self.fils[1] is not None:
                yield from self.fils[1].iterate(min, max)