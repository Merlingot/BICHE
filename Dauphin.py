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
        xlim, ylim : np.array([min,max])
    """
    def __init__(self, panda, poulpe, dt, dq, xlim, ylim, nt):
        self.panda = panda
        self.poulpe = poulpe
        self.nt = nt
        self.dt = dt # time step
        self.dq = dq # space step
        self.xmin, self.xmax = xlim[0], xlim[1]
        self.ymin, self.ymax = ylim[0], ylim[1]

    def solve(self):
        """
        Solve for N time steps
        """
        if isinstance(self.nt, np.int64) :
            dt = self.dt
            dq = self.dq
            N = self.nt
        elif  isinstance(self.nt, int):
            dt = self.dt
            dq = self.dq
            N = self.nt
        else:
            dt = self.dt.get()
            dq = self.dq.get()
            N = self.nt.get()
        self.panda.initialize_data()

        epsilonE = 0.0002
        positions = np.zeros([N,2])
        velocities = np.zeros([N,2])
        energies = np.zeros([N])
        # n=0
        n=0
        positions[n,:] = self.panda.pos0
        velocities[n,:] = self.panda.vit0
        energies[n] = 0.5*self.panda.mass*norm(self.panda.vit0)**2 - self.poulpe.compute_field(self.panda.pos0)@self.panda.m
        # tn=1 step -------------------------------------------------
        n=1
        pos1, vit1 = verlet_step_1(self.panda, self.poulpe, dt, dq, self.xmin, self.xmax, self.ymin, self.ymax)
        positions[n,:] = pos1
        velocities[n,:] = vit1
        energies[n] = 0.5*self.panda.mass*norm(vit1)**2 - self.poulpe.compute_field(pos1)@self.panda.m
        # n>1 steps ------------------------------------------------
        if N > 1:
            for i in range(N-2):
                n +=1
                posNplus1, vitNplus1 = verlet_step_n(self.panda, self.poulpe, dt, dq, self.xmin, self.xmax, self.ymin, self.ymax)
                positions[n,:] = posNplus1
                velocities[n,:] = vitNplus1
                energies[n] = 0.5*self.panda.mass*norm(vitNplus1)**2 - self.poulpe.compute_field(posNplus1)@self.panda.m
                if (energies[n]-energies[n-1])>0:
                    dt = dt*(energies[n]-energies[n-1])/energies[n]

        if self.panda.varpos:
            self.panda.graph_link.update_position(self.panda.graph)
            arr = positions
            self.panda.graph.axes.plot(arr[:,0], arr[:,1])
            self.panda.graph.update_graph()

        return positions, velocities, energies

def puck_outside(posNplus1, xmin, xmax, ymin, ymax):
    """ Check if the position of the puck is outside the limits.
    If is outside, return True """
    if  posNplus1[0]<xmin or posNplus1[0]>xmax or ymin>posNplus1[1] or posNplus1[0]>ymax:
        return True


def calculate_force(panda, pos, poulpe, dq):
    """Calculates the energy derivatives in x and y in space at the position pos. FORCE!!
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
    derivativeX = ( poulpe.compute_field(pos+vecdqX)@panda.m -poulpe.compute_field(pos-vecdqX)@panda.m )/(2*dq)
    derivativeY = ( poulpe.compute_field(pos+vecdqY)@panda.m -poulpe.compute_field(pos-vecdqY)@panda.m)/(2*dq)
    vecDerivative = (-1)*np.array([derivativeX, derivativeY])
    return vecDerivative


def verlet_step_1(panda, poulpe, dt, dq, xmin, xmax, ymin, ymax):
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
    force0=calculate_force(panda,panda.pos, poulpe, dq)
    pos1 = panda.pos + panda.vit*dt +(0.5)*(dt**2)*force0/panda.mass
    # Update position
    panda.update_pos(pos1)
    # Calcul vitesse
    force1 = calculate_force(panda, panda.pos, poulpe, dq)
    vit1 = panda.vit + 0.5*dt*(force0 + force1)/panda.mass
    # Update velocity
    panda.update_vit(vit1)
    # outside ?
    # if puck_outside(pos1, xmin, xmax, ymin, ymax):
    #     pass
    return panda.pos, panda.vit

def verlet_step_n(panda, poulpe, dt, dq, xmin, xmax, ymin, ymax):
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
    forceN=calculate_force(panda, panda.pos, poulpe, dq)
    posNplus1 = 2*panda.pos - panda.lastPos + (dt**2)*forceN/panda.mass
    # Update position
    panda.update_pos(posNplus1)
    # calculer vitesse
    forceNplus1 = calculate_force(panda, panda.pos, poulpe, dq)
    vitNplus1 = panda.vit + 0.5*dt*(forceN + forceNplus1)/panda.mass
    # Update velocity
    panda.update_vit(vitNplus1)
    # outside ?
    # if puck_outside(posNplus1, xmin, xmax, ymin, ymax):
    #     pass
    return panda.pos, panda.vit






# def space_derivative_energy(panda, poulpe, dq):
#     """Calculates the energy derivatives in x and y in space at the position pos. FORCE!!
#     Derivative :
#             U(q) = -m@B(q) -> U(q+dq)=-m@B(q+dq)
#             dU/dq_i = (-1)*( m@B(q+dq_i) - m@B(q - dq_i) )/(2*dq_i)
#     Args:
#         pos : np.array([qx,qy])
#         dq : float
#         m : np.array([mx, my, mz])
#     Returns:
#         vecDerivative : np.array([dB/dx, dB/dy])
#                         Derivatives of B in direction x and y at point pos.
#     """
#     vecdqX = np.array([dq,0])
#     vecdqY = np.array([0,dq])
#     derivativeX = np.divide((poulpe.compute_field(panda.pos+vecdqX)@panda.m-poulpe.compute_field(panda.pos-vecdqX)@panda.m ),2*dq)
#     derivativeY = np.divide( poulpe.compute_field(panda.pos+vecdqY)@panda.m
#                             -poulpe.compute_field(panda.pos-vecdqY)@panda.m,2*dq)
#     vecDerivative = (-1)*np.array([derivativeX, derivativeY])
#     return vecDerivative
#
#
# def verlet_step_1(panda, poulpe, dt, dq, xmin, xmax, ymin, ymax):
#     """First step of Verlet integration
#     Calculates position at time n=1 from intial conditions
#
#     q1 = q0 + v0*dt + 0.5*dt^2*dU(q0)/dq
#
#     Args: panda (Panda)
#         poulpe (Poulpe)
#         dt (float) : time step
#         dq (float) : space step
#     Returns:
#         pos1 : np.array([qx, qy])
#     """
#     force0=space_derivative_energy(panda, poulpe, dq)
#     pos1 = panda.pos + np.multiply(panda.vit,dt)
#     pos1 += (0.5)*(dt**2)*np.divide(force0, panda.mass)
#     if puck_outside(pos1, xmin, xmax, ymin, ymax):
#         reflection(panda, pos1, xmin, xmax, ymin, ymax)
#     else:
#         # Update position
#         panda.update_pos(pos1)
#         # Calcul vitesse
#         force1 = space_derivative_energy(panda, poulpe, dq)
#         vit1 = panda.vit + np.divide(0.5*dt*(force0 + force1),panda.mass)
#         # Update velocity
#         panda.update_vit(vit1)
#         # outside ?
#     return panda.pos
#
# def verlet_step_n(panda, poulpe, dt, dq, xmin, xmax, ymin, ymax):
#     """ Step n>1 of Verlet integration
#     Calculates next position from current position
#
#     qn+1 = 2*qn - qn-1 + dt^2*dU(qn)/dq
#
#     Args:
#         panda (Panda)
#         poulpe (Poulpe)
#         dt (float) : time step
#         dq (float) : space step
#     Returns:
#         posn : np.array([qx, qy])
#     """
#     forceN=space_derivative_energy(panda, poulpe, dq)
#     posNplus1 = 2*panda.pos - panda.lastPos + (dt**2)*(forceN)/panda.mass
#
#     # outside ?
#     if puck_outside(posNplus1, xmin, xmax, ymin, ymax):
#         reflection(panda, posNplus1, xmin, xmax, ymin, ymax)
#     else:
#         # Update position
#         panda.update_pos(posNplus1)
#         # calculer vitesse
#         forceNplus1 = space_derivative_energy(panda, poulpe, dq)
#         vitNplus1 = panda.vit + 0.5*dt*(forceN + forceNplus1)/panda.mass
#         # Update velocity
#         panda.update_vit(vitNplus1)
#     return panda.pos
