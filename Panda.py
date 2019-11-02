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
        self.pos = None
        self.vit = None
        self.lastPos = None
        self.lastVit = None
        self.storePos = []
        self.storeVit = []

    def update_pos(currentPos, newPos):
        """
        Store current position
        Set current position as last position
        Set new posiiton as current position
        """
        self.storePos.append(currentPos)
        self.lastPos = currentPos
        self.pos = newPos

    def update_vit(currentVit, newVit):
        self.storeVit.append(currentVit)
        self.lastVit = currentVit
        self.vit = newVit
