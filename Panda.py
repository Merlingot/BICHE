class Panda:

    def __init__(self, pos0, vit0, m, mass=1):
        """
        pos0 : np.array([qx,qy])
                Initial position
        vit0 = np.array([vx,vy])
                Initial velocity
        m = np.array([0,0,mz])
            Moment dipolaire
        """
        self.varpos = pos0
        self.varvit = vit0
        self.varm = m
        self.varmass = mass
        self.pos0 = [0, 0]
        self.vit0 = [0, 0]
        self.m = 1
        self.mass = 1
        self.pos = pos0
        self.vit = vit0
        self.lastPos = None
        self.lastVit = None
        self.storePos = [0, 0]
        self.storeVit = [0, 0]
        self.graph_link = None
        self.graph = None

    def initialize_data(self):

        self.pos0 = [self.varpos[0].get(), self.varpos[1].get()]
        self.pos = self.pos0
        self.storePos = [self.pos0]
        self.vit0 = [self.varvit[0].get(), self.varvit[1].get()]
        self.vit = self.vit0
        self.storeVit = [self.vit0]
        self.m = self.varm.get()
        self.mass= self.varmass.get()

    def update_pos(self, newPos):
        """
        Store current position
        Set current position as last position
        Set new position as current position
        """
        self.lastPos = self.storePos[-1]
        self.pos = newPos
        self.varpos[0].set(self.pos[0])
        self.varpos[1].set(self.pos[1])
        self.storePos.append(self.pos)
        self.graph_link.update_position(self.graph)

    def update_vit(self, newVit):
        self.lastVit = self.storeVit[-1]
        self.vit = newVit
        self.varvit[0].set(self.vit[0])
        self.varvit[1].set(self.vit[1])
        self.storeVit.append(self.vit)

    def clear_panda(self):
        self.pos = self.pos0
        self.vit = self.vit0
        self.lastPos = None
        self.lastVit = None
        self.storePos = [self.pos0]
        self.storeVit = [self.vit0]
