import numpy as np
import tkinter as tk

class Pos:
    def __init__(self):
        self.x = np.array([0,1])

    def setX(self,_x):
        self.x = _x

    def getX(self):
        return self.x

class Ane:
    def __init__(self):
        self.pos = Pos()
        self.vit = 1
        print("hihaaAAA")

    def __str__(self):
        return "pos: "+str(self.pos)+" vit: "+str(self.vit)

    def setPos(self,_pos):
        self.pos.setX(_pos)

class Chevau:

    def __init__(self,ane):
        self.pos = ane.pos.getX()
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
