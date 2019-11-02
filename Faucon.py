from Poulpe import *
from Panda import *
from Dauphin import *
from OurangOutan import *

## Classe agissant comme Overhead de l'algorithme de resolution

class Faucon:

	#Valeurs par défault (initiales) des paramètres numériques


	# Constructeur
	def __init__(self, lionceau,dictHyene,course, vision,fourmi):
		self.nt = fourmi.nt
		self.poulpe = Poulpe(vision)
		self.dictHyeneToPoulpe(dictHyene)
		self.panda = Panda(lionceau.pos, lionceau.vit, lionceau.force)
		self.dauphin = Dauphin(panda, poulpe, fourmi.dt,fourmi.dq)

	def run_simulation(self, nt):
		dauphin.solve(nt)

#Transforme un dictionnaire de Hyene en liste de Calmar et le set comme liste de calmars de poulpe
	def dict_hyene_to_poulpe(self,dictHyene):
		calmarList = []
		for key in dictHyene:
			calmarList.append(Calmar(dictHyene[key].force,dictHyene[key].pos))
			self.poulpe.setCalmars(calmarList)

	#Mise a jour du graphique
	def update_graphB(self):
		self.poulpe.updateMesh()
