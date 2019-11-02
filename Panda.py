class Panda:

    def __init__(self, pos, vit, m):
        """
        pos = np.array([qx,qy])
        vit = np.array([vx,vy])
        m = np.array([0,0,mz])
        """
        self.pos = pos
        self.vit = vit
        self.m = m
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
