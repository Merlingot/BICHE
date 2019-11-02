import Poulpe
import Panda
import Dauphin


## Classe agissant comme Overhead de l'algorithme de resolution

class Faucon:

	#Valeurs par défault (initiales) des paramètres numériques
	dt = 0.1
	dx = 0.1
	epsilon = 0.001

	# Constructeur
	def __init__(lionceau,dictHyene):
		poulpe = Poulpe()
		poulpe.add(dictHyeneToCalmarList(dictHyene))
		panda = Panda(lionceau)
		dauphin = Dauphin(Panda, Poulpe, dt,dx)

#Transforme un dictionnaire de Hyene en liste de Calmar
def dictHyeneToCalmarList(dictHyene):
	calmarList = []
	for key in dictHyene:
		calmarList.append(Calmar(dictHyene[key].force,dictHyene[key].pos))
