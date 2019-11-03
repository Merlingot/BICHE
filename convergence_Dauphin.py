import numpy as np
from Dauphin import Dauphin
from Panda import Panda
from Poulpe2 import Poulpe


panda = Panda()
poulpe = Poulpe()

# Convergence Temporelle
dq = 1e-3
Lt = 100 #secondes
Nts = np.arange(10,100,5)
vec_dt = np.zeros(len(Nts))
errdt = np.zeros(len(Nts))

for indexdt in range(len(Nts)): # index sur les Nt
    Nt = Nts[indexdt] #nbre de points de temps
    Nt2 = Nt*2
    dt = Lt/Nt
    dt2 = Lt/Nt2
    vec_dt[indexdt] = dt

    dauphin = Dauphin(panda, poulpe, dq, dt)
    dauphin2 = Dauphin(panda, poulpe, dq, dt2)

    dauphin.solve(Nt)
    dauphin2.solve(Nt2)

    sol = np.array(dauphin.panda.storePos)
    sol2 = np.array(dauphin2.panda.storePos)

    errxy=0
    for t in range(Nt): #indice sur le temps
        errxy += np.linalg.norm(sol[t] - sol2[t])
    errdt[indexdt] = errxy





# # Convergence Spatiale
# dt = 1e-3
# Lt = 100 #secondes
# dQs = linspace(1e-6,1e-3,10)
# vec_dq = np.zeros(len(dQs))
# errdq = np.zeros(len(dQs))
#
# for indexdt in range(len(Nts)): # index sur les Nt
#     Nt = Nts[indexdt] #nbre de points de temps
#     Nt2 = Nt*2
#     dt = Lt/Nt
#     dt2 = Lt/Nt2
#     vec_dt[indexdt] = dt
#
#     dauphin = Dauphin(panda, poulpe, dq, dt)
#     dauphin2 = Dauphin(panda, poulpe, dq, dt2)
#
#     dauphin.solve(Nt)
#     dauphin2.solve(Nt2)
#
#     sol = np.array(dauphin.panda.storePos)
#     sol2 = np.array(dauphin2.panda.storePos)
#
#     errxy=0
#     for t in range(Nt): #indice sur le temps
#         errxy += np.linalg.norm(sol[t] - sol2[t])
#     errdt[indexdt] = errxy
