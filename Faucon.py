import Poulpe
import Panda
import Dauphin
from OurangOutan import * 

## Classe agissant comme Overhead de l'algorithme de resolution

class Faucon:

	#Valeurs par défault (initiales) des paramètres numériques
	dt = 0.1
	dx = 0.1

	# Constructeur
	def __init__(lionceau,dictHyene,course, vision):
		poulpe = Poulpe(vision)
		self.dictHyeneToPoulpe(dictHyene)
		panda = Panda(lionceau.pos, lionceau.vit, lionceau.force)
		dauphin = Dauphin(panda, poulpe, dt,dx)

#Transforme un dictionnaire de Hyene en liste de Calmar et le set comme liste de calmars de poulpe
def dictHyeneToPoulpe(self,dictHyene):
	calmarList = []
	for key in dictHyene:
		calmarList.append(Calmar(dictHyene[key].force,dictHyene[key].pos))
	self.poulpe.setCalmars(calmarList)
