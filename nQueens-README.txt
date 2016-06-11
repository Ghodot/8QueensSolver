Copyright Nicolas Dol , 2016


Ce programme a été réalisé à l'aide du language python 2.7, et est destiné à être exécuter par cette version de python.
Il résout le problème des n-dames, qui consiste à placer n dames sur un échiquier d'une taille définie sans que celles-ci ne s'attaquent.


Le fichier prend 3 arguments en entrée lors de son appel, dans l'ordre :

	- Le nombre de dames à placer. Celui-ci peut être supérieur à la taille de l'échiquier
	- La taille de l'échiquer, c'est à dire sa largeur/longueur en nombre de cases
	- Enfin, le nombre d'itérations max que l'algorithme va effectuer avant d'arrêter la recherche d'une solution


L'algorithme s'arrête lorsqu'il a trouvé une solution au problème (aucune reine ne s'attaque).
Sinon, il continue de tourner jusqu'à $nombreIterations et renvoie la meilleure solution trouvée (le moins de reines en confrontation)

La méthode de recuit simulé utilisé est fortement dépendante de la température actuelle de l'algorithme, qui décroit linéairement en fonction du nombre d'itérations max
Ainsi, mettre plus d'itérations peut augmenter le nombre de temps pour trouver une solution, mais il est plus probable de trouver une solution.