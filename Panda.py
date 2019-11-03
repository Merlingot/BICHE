class Panda:

    def __init__(self, pos0, vit0, m, mass=1):
        """
        pos0 : DoubleVar()
                Initial position
        vit0 = DoubleVar()
                Initial velocity
        m = DoubleVar()
            Moment dipolaire
        mass = DoubleVar()
            Masse du dipole
        """
        self.pos0Var = pos0
        self.vit0Var = vit0
        self.mVar = m
        self.massVar=mass
        self.lastPos = None
        self.lastVit = None


    def update_pos(self, newPos):
        """
        Store current position
        Set current position as last position
        Set new position as current position
        """
        self.lastPos = self.storePos[-1]
        self.pos = newPos
        self.storePos.append(self.pos)


    def update_vit(self, newVit):
        self.lastVit = self.storeVit[-1]
        self.vit = newVit
        self.storeVit.append(self.vit)

    def clear_panda(self):
        self.pos = self.pos0
        self.vit = self.vit0
        self.lastPos = None
        self.lastVit = None
        self.storePos = [self.pos0]
        self.storeVit = [self.vit0]

    """
    Prépare le panda à l'aventure en transformant les DoubleVar en np.array
    """
    def panda_attaque(self):
        self.pos0 = np.array([self.pos0Var[0].get(),self.pos0Var[1].get()])
        self.vit0 = np.array([self.vit0Var[0].get(),self.vit0Var[1].get()])
        self.m = self.mVar.get()
        self.mass=self.massVar.get()
        self.pos = self.pos0
        self.vit = self.vit0
        self.storePos = [self.pos0]
        self.storeVit = [self.vit0]
