import Poulpe
import Panda
import Dauphin
from OurangOutan import *

## Classe agissant comme Overhead de l'algorithme de resolution

class Faucon:

	#Valeurs par défault (initiales) des paramètres numériques


	# Constructeur
	def __init__(lionceau,dictHyene,course, vision,dt,dq,nt):
		self.nt = nt
		self.poulpe = Poulpe(vision)
		self.dictHyeneToPoulpe(dictHyene)
		self.panda = Panda(lionceau.pos, lionceau.vit, lionceau.force)
		self.dauphin = Dauphin(panda, poulpe, dt,dq)

	def runSimulation(nt):
		dauphin.solve(nt)

#Transforme un dictionnaire de Hyene en liste de Calmar et le set comme liste de calmars de poulpe
def dictHyeneToPoulpe(self,dictHyene):
	calmarList = []
	for key in dictHyene:
		calmarList.append(Calmar(dictHyene[key].force,dictHyene[key].pos))
	self.poulpe.setCalmars(calmarList)

#Mise a jour du graphique
def updateGraphB(self):
	self.poulpe.updateMesh()
