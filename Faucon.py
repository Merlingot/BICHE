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
	def __init__(_lionceau,_dictHyene):

		poulpe = Poulpe()
		panda = Panda(_lionceau)
		dauphin = Dauphin(Panda, Poulpe, dt,dx)

	def dictHyeneToCalmarList(_dictHyene)
