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
        self.pos0 = pos0
        self.vit0 = vit0
        self.pos=pos0
        self.vit=vit0
        self.m= m
        self.mass=mass
        self.lastPos = None
        self.lastVit = None
        self.storePos = [self.pos0]
        self.storeVit = [self.vit0]
        # self.panda_attaque()


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

    def reflection(self, xmin, xmax, ymin, ymax):
        """ Changes posNplus1 and vitNplus1 for reflection """

        x = self.pos[0] #qnplus1
        y = self.pos[1] #qnplus1
        vx = self.vit[0]
        vy = self.vit[1]

        print("x: "+ str(x)+" xmax: "+str(xmax)+" y: "+str(y)+" ymax: "+str(ymax))

        if x>=xmax:
            self.pos[0] = 2*xmax - x
            self.vit[0] = -vx
        elif x<=xmin:
            self.pos[0] = 2*xmin - x
            self.vit[0] = -vx
        if y>=ymax:
            self.pos[1] = 2*ymax - y
            self.vit[1] = -vy
        elif y<=ymin:
            self.pos[1] = 2*ymin - y
            self.vit[1] = -vy

        #Corriger les array
        self.storePos[-1]=self.pos
        self.storePos[-1]=self.vit


    """
    Prépare le panda à l'aventure en transformant les DoubleVar en np.array
    """
    # def panda_attaque(self):
    #     # self.pos0 = np.array([self.pos0Var[0].get(),self.pos0Var[1].get()])
    #     # self.vit0 = np.array([self.vit0Var[0].get(),self.vit0Var[1].get()])
    #     self.m = self.mVar
    #     self.mass=self.massVar
    #     self.pos = self.pos0Var
    #     self.vit = self.vit0Var
    #     self.storePos = [self.pos0Var]
    #     self.storeVit = [self.vit0Var]
