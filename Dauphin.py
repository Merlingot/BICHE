import numpy as np
from Panda import Panda
from Poulpe import Poulpe

from numpy.linalg import norm

## classe objet du solveur

class Dauphin:

    """
    Desc: Solveur Verlet

    Parametres:
        Panda : Puck bougeants
        Poulpe : Outils pour le magnetic field
        dt : discretisation en temps
        dq : discretisation de l'espace
    """
    def __init__(self, panda, poulpe, dt, dq):
        self.panda = panda
        self.poulpe = poulpe
        self.dt = dt # time step
        self.dq = dq # space step

    def solve(N):
        """
        Solve for N time steps
        """
        # n=1 step -------------------------------------------------
        # Calculate next position (and velocity - TO DO)
        pos1 = verletStep1(self.panda, self.poulpe, self.dt, self.dq)
        # Update position (and velocity - TO DO)
        self.panda.update_pos(self.panda.pos0, pos1)
        # n>1 steps ------------------------------------------------
        if N > 1:
            for n in range(N-1):
                # Calculate next position (and velocity - TO DO)
                posn = verletStepN(self.panda, self.pouple, self.dt, self.dq)
                # Update position (and velocity - TO DO)
                self.panda.update_pos(self.panda.pos, posn)
        return 1


def spaceDerivativeEnergy(panda, poulpe, dq):
    """Calculates the energy derivatives in x and y in space at the position pos.
    Derivative :
            U(q) = -m@B(q) -> U(q+dq)=-m@B(q+dq)
            dU/dq_i = (-1)*( m@B(q+dq_i) - m@B(q - dq_i) )/(2*dq_i)
    Args:
        pos : np.array([qx,qy])
        dq : float
        m : np.array([mx, my, mz])
    Returns:
        vecDerivative : np.array([dB/dx, dB/dy])
                        Derivatives of B in direction x and y at point pos.
    """
    vecdqX = np.array([dq,0])
    vecdqY = np.array([0,dq])
    derivativeX = ( poulpe.compute_field(panda.pos+vecdqX)@panda.m -poulpe.compute_field(panda.pos-vecdqX)@panda.m )/(2*dq)
    derivativeY = ( poulpe.compute_field(panda.pos+vecdqY)@panda.m -poulpe.compute_field(panda.pos-vecdqY)@panda.m)/(2*dq)
    vecDerivative = (-1)*np.array([derivativeX, derivativeY])
    return vecDerivative


def verletStep1(panda, poulpe, dt, dq):
    """First step of Verlet integration
    Calculates position at time n=1 from intial conditions

    q1 = q0 + v0*dt + 0.5*dt^2*dU(q0)/dq

    Args:
        panda (Panda)
        poulpe (Poulpe)
        dt (float) : time step
        dq (float) : space step
    Returns:
        pos1 : np.array([qx, qy])
    """
    pos1 = panda.pos + panda.vit*dt +(0.5)*(dt**2)*spaceDerivativeEnergy(panda, poulpe, dq)
    return pos1

def verletStepN(panda, pouple, dt, dq):
    """ Step n>1 of Verlet integration
    Calculates next position from current position

    qn+1 = 2*qn - qn-1 + dt^2*dU(qn)/dq

    Args:
        panda (Panda)
        poulpe (Poulpe)
        dt (float) : time step
        dq (float) : space step
    Returns:
        posn : np.array([qx, qy])
    """
    posn = 2*panda.pos - panda.lastPos + (dt**2)*spaceDerivativeEnergy(panda, poulpe, dq)
    return posn
