Copyright Nicolas Dol , 2016


Ce programme a �t� r�alis� � l'aide du language python 2.7, et est destin� � �tre ex�cuter par cette version de python.
Il r�sout le probl�me des n-dames, qui consiste � placer n dames sur un �chiquier d'une taille d�finie sans que celles-ci ne s'attaquent.


Le fichier prend 3 arguments en entr�e lors de son appel, dans l'ordre :

	- Le nombre de dames � placer. Celui-ci peut �tre sup�rieur � la taille de l'�chiquier
	- La taille de l'�chiquer, c'est � dire sa largeur/longueur en nombre de cases
	- Enfin, le nombre d'it�rations max que l'algorithme va effectuer avant d'arr�ter la recherche d'une solution


L'algorithme s'arr�te lorsqu'il a trouv� une solution au probl�me (aucune reine ne s'attaque).
Sinon, il continue de tourner jusqu'� $nombreIterations et renvoie la meilleure solution trouv�e (le moins de reines en confrontation)

La m�thode de recuit simul� utilis� est fortement d�pendante de la temp�rature actuelle de l'algorithme, qui d�croit lin�airement en fonction du nombre d'it�rations max
Ainsi, mettre plus d'it�rations peut augmenter le nombre de temps pour trouver une solution, mais il est plus probable de trouver une solution.