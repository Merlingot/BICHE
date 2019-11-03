class Panda:

    def __init__(self, pos0, vit0, m):
        """
        pos0 : np.array([qx,qy])
                Initial position
        vit0 = np.array([vx,vy])
                Initial velocity
        m = np.array([0,0,mz])
            Moment dipolaire
        """
        self.pos0 = pos0
        self.vit0 = vit0
        self.m = m
        self.pos = pos0
        self.vit = vit0
        self.lastPos = None
        self.lastVit = None
        self.storePos = []
        self.storeVit = []

    def update_pos(self, newPos):
        """
        Store current position
        Set current position as last position
        Set new posiiton as current position
        """
        self.storePos.append(self.pos)
        self.lastPos = self.storePos[-1]
        self.pos = newPos

    def update_vit(self, newVit):
        self.storeVit.append(self.pos)
        self.lastVit = self.storeVit[-1]
        self.vit = newVit

    def clear_panda(self):
        self.pos = self.pos0
        self.vit = self.vit0
        self.lastPos = None
        self.lastVit = None
        self.storePos.clear()
        self.storeVit.clear()
