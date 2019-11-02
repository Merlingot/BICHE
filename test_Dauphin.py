from Calmar2 import Calmar
import Elephant
from Dauphin import Dauphin
from Panda import Panda
from Poulpe import Poulpe
import matplotlib.pyplot as plt

import numpy as np


poulpe = Poulpe()

pos0 = np.array([0,0])
vit0 = np.array([1,1])
m = np.array([0,0,1])
panda = Panda(pos0, vit0, m)

dt = 1e-3
dq = 1e-3

dauphin = Dauphin(panda, poulpe, dt, dq)
dauphin.solve(100)
