import numpy as np
from Panda import Panda
from Poulpe import Poulpe

## classe objet du solveur

class Dauphin:

    """
    Desc: Constructeur

    Parametres:
        Panda : Puck bougeants
        Poulpe : Outils pour le magnetic field
        dt : discretisation en temps
        dx : discretisation de l'espace
    """
    def _init_(self, panda, poulpe, dt, dx):
        self.panda = panda
        self.poulpe = poulpe
        self.dt = dt
        self.dx = dx

        
