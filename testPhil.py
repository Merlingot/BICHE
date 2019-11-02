import numpy as np
class Ane:
    pos = [1,2]
    vit = 1

    def __init__(self):
        print("hihaaAAA")

    def __str__(self):
        return "pos: "+str(self.pos)+" vit: "+str(self.vit)

    def setPos(self,_pos):
        self.pos = _pos

class Chevau:

    def __init__(self,ane):
        self.pos = ane.pos
        self.vit = ane.vit

    def __str__(self):
        return "pos: "+str(self.pos)+" vit: "+str(self.vit)

ane = Ane()
print(ane)
chevau = Chevau(ane)
print(chevau)
ane.setPos(np.array([4,5]))
print(ane)
print(chevau)
