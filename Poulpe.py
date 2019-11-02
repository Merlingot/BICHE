import numpy as np

from Calmar import Calmar

## Classe utiliser pour obtenir le champs magnetique en tout point grace a une liste de aimants (Calmar)

############## SSSSSSSSQQQQQQQQQQQQUUUUUUUUUIIIIIIIIIIIIDDDDDDDDDDDDD ###################

class Poulpe:

	
    def __init__(self):
        
        self.listeCalmar = []

    """
    Desc : Ajoute un aimant a la liste d'aimant

    Parametres:
        pos : position de l'aimant a ajouter
        m : Aimantation de l'aimant a ajouter a la table
    """
    def add_calmar(self, pos, m):

        self.listeCalmar.append( Calmar(pos, m) )

    """
    Desc : Calcule le champs totale de tous les aimant a un point pos

    Parametres:
        pos : position du champs desire
        RETURN : retourne un numpy array du champs total de tous les aimants
    """
    def compute_field(self, pos ):

        Btot = np.array([0.,0.,0.]) 

        for calmar in self.listeCalmar:
            
            Btot += calmar.compute_contribution(pos)

        return Btot



