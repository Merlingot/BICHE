import numpy as np
from Poulpe import Poulpe
from Calmar import Calmar
import Elephant

##########################################################################
# Creation d'un poulpe

poulpe = Poulpe()

# Calcul de la contribution de 0 aimant, on devrait avoir B = 0

Btot = poulpe.compute_field(np.array([0.,0.]))

print(Btot)

##########################################################################
# Add un aimant

poulpe.add_calmar(10., np.array([0.,0.]))

# Recompute total field, on ne devrait pas avoir 0

Btot = poulpe.compute_field(np.array([0.,0.]))

print(Btot)

###########################################################################
# Ajout d'une liste de Calmars

cal = [Calmar(100., np.array([2.,2.])), Calmar(1000., np.array([0.,1.])) ]

poulpe.add_calmar_liste(cal)

# Calcul du nouveau champs

Btot = poulpe.compute_field(np.array([0.,0.]))

print(Btot)


