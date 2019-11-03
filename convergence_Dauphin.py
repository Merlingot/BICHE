@@ -7,6 +7,7 @@ from Poulpe2 import Poulpe
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy.linalg import norm


# POOOOUUUUUUUUUULLLLLPPPPPPPPPPEEEEEEEEEEEE
@ -17,20 +18,20 @@ poulpe.add_calmar(10, np.array([0,1e-1]))

# PPPAAAAAAANNNNNNNNDDDDDDDAAAAAAAAAAA
pos0 = np.array([0,0])
vit0 = np.array([1e-5,0])
vit0 = np.array([1e-3,0])
m = np.array([0,0,1])
panda = Panda(pos0, vit0, m)
panda2 = Panda(pos0, vit0, m)

# # Convergence Temporelle
dq = 1e-1
Lt = 1
dq = 2**(-11)
Lt = 2
Nts = np.power(2, np.arange(3,13)) #Differents nombre de points
dts = np.zeros(len(Nts)) #dt pour les differents nombre de points
errsdt = np.zeros(len(Nts)) #erreurs pour les differents nombre de points
errsvit = np.zeros(len(Nts))
xlim = np.array([-100,100])
ylim = np.array([-100,100])
xlim = np.array([-1e-3,1e-3])
ylim = np.array([-1e-3,1e-3])

for indexdt in range(len(Nts)): # index sur les Nt
    Nt = Nts[indexdt] #nbre de points de temps
@ -75,16 +76,45 @@ plt.figure()
plt.title('Analyse de convergence temporelle')
plt.xlabel('dt')
plt.ylabel('Erreur')
plt.loglog(dts, np.exp(f(dts, popt[0], popt[1])))
plt.loglog(dts, np.exp(f(dts, poptV[0], poptV[1])))
plt.loglog(dts, np.exp(f(dts, popt[0], popt[1])), label='Positon')
plt.loglog(dts, np.exp(f(dts, poptV[0], poptV[1])), label='Vitesse')
plt.loglog(dts, errsdt, 'o')
plt.loglog(dts, errsvit, 'x')
plt.legend()
plt.show()

# plt.figure()
# plt.title('Espace des phases (Analyse de convergence temporelle)')
# plt.xlabel('q')
# plt.ylabel('p')
# plt.plot(norm(sol2, axis=1), norm(vit2, axis=1))
# plt.show()
#
# plt.figure()
# plt.title('Espace des phases (Analyse temporelle)')
# plt.xlabel('qx')
# plt.ylabel('px')
# plt.plot(sol2[:,0], vit2[:,0])
# plt.show()
#
# plt.figure()
# plt.title('Espace des phases (Analyse temporelle)')
# plt.xlabel('qy')
# plt.ylabel('py')
# plt.plot(sol2[:,1], vit2[:,1])
# plt.show()

plt.figure()
plt.title('Trajectoire (Analyse spatiale)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(sol2[:,0], sol2[:,1], 'o')
plt.show()



# Convergence Spatiale (attention aux PPPAAAAAAANNNNNNNNDDDDDDDAAAAAAAAAAAs)
Lt=1
Lt=2
Nt = int(2**10)
dt = Lt/Nt
dqs = np.array([2**(-11), 2**(-10), 2**(-9), 2**(-8), 2**(-7), 2**(-6),2**(-5)]) #Differents nombre de points
@ -98,8 +128,8 @@ for indexdq in range(len(dqs)): # index sur les dq
    dq = dqs[indexdq]
    dq2 = dqs[indexdq]/2

    dauphin = Dauphin(panda, poulpe, dt, dq,xlim,ylim)
    dauphin2 = Dauphin(panda2, poulpe, dt, dq2,xlim,ylim)
    dauphin = Dauphin(panda, poulpe, dt, dq, xlim,ylim)
    dauphin2 = Dauphin(panda2, poulpe, dt, dq2, xlim,ylim)

    dauphin.solve(Nt)
    dauphin2.solve(Nt)
@ -134,8 +164,39 @@ plt.figure()
plt.title('Analyse de convergence spatiale')
plt.xlabel('dq')
plt.ylabel('Erreur')
plt.loglog(dqs, np.exp(f(dqs, popt[0], popt[1])))
plt.loglog(dqs, np.exp(f(dqs, popt[0], popt[1])), label='Position')
plt.loglog(dqs, errsdq, 'o')
plt.loglog(dqs, np.exp(f(dqs, poptV[0], poptV[1])))
plt.loglog(dqs, np.exp(f(dqs, poptV[0], poptV[1])), label='Vitesse')
plt.loglog(dqs, errsvit, 'x')
plt.legend()
plt.show()


plt.figure()
plt.title('Trajectoire (Analyse spatiale)')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(sol2[:,0], sol2[:,1], 'o')
plt.show()


# plt.figure()
# plt.title('Espace des phases (Analyse spatiale)')
# plt.xlabel('q')
# plt.ylabel('p')
# plt.plot(norm(sol2, axis=1), norm(vit2, axis=1))
# plt.show()
#
# plt.figure()
# plt.title('Espace des phases (Analyse temporelle)')
# plt.xlabel('qx')
# plt.ylabel('px')
# plt.plot(sol2[:,0], vit2[:,0])
# plt.show()
#
# plt.figure()
# plt.title('Espace des phases (Analyse temporelle)')
# plt.xlabel('qy')
# plt.ylabel('py')
# plt.plot(sol2[:,1], vit2[:,1])
# plt.show()
