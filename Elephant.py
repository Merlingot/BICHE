import scipy.constants as sciconst

PI = sciconst.pi
MU0 = sciconst.mu_0

# PARAMETRES !!!
dq = 1e-8
dt=1e-8
masse = 100e-3
mz=1e-2
# POOOOUUUUUUUUUULLLLLPPPPPPPPPPEEEEEEEEEEEE
poulpe = Poulpe()
poulpe.add_calmar(2, np.array([0,5e-1]))
# poulpe.add_calmar(-10, np.array([0.5,0.5]))
# poulpe.add_calmar(50, np.array([1,1]))

# PPPAAAAAAANNNNNNNNDDDDDDDAAAAAAAAAAA
pos0 = np.array([0,0])
vit0 = np.array([2e-2,0])
m = np.array([0,0,mz])
