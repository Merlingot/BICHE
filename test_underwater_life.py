import numpy as np
import tkinter as tk
root = tk.Tk()
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

pos = np.array([tk.DoubleVar(), tk.DoubleVar()])
pos[0].set(1)
pos[1].set(1)
m = tk.DoubleVar()
m.set(10)
poulpe.add_calmar(m, pos)

# Recompute total field, on ne devrait pas avoir 0

Btot = poulpe.compute_field(np.array([0.,0.]))

print(Btot)

###########################################################################
# Ajout d'une liste de Calmars

pos1 = np.array([tk.DoubleVar(), tk.DoubleVar()])
pos1[0].set(1)
pos1[1].set(1)
m1 = tk.DoubleVar()
m1.set(10)

pos2 = np.array([tk.DoubleVar(), tk.DoubleVar()])
pos2[0].set(1)
pos2[1].set(1)
m2 = tk.DoubleVar()
m2.set(10)

cal = [Calmar(m1,pos1), Calmar(m2,pos2) ]

poulpe.add_calmar_liste(cal)

# Calcul du nouveau champs

Btot = poulpe.compute_field(np.array([0.,0.]))

print(Btot)


