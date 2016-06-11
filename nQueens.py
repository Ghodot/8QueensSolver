from __future__ import print_function

import numpy as np
import random
import copy
import math
import sys



def initialisationGrille(tailleGrille):
	grille = np.zeros((tailleGrille,tailleGrille))
	return(grille)

def solutionInitiale(n,tailleGrille):
	sol = np.zeros((n,tailleGrille,tailleGrille))
	dejaPlaces = []
	for i in range(n):
		dejaPlaces.append((i,i))
	return(dejaPlaces)

#On place des 1 aux endroits interdits
def casesInterdites(reines,tailleGrille):
	grille = initialisationGrille(tailleGrille)
	for reineActuelle in reines:
		x = reineActuelle[0]
		y = reineActuelle[1]
		# On memorise la valeur de la case avant de "poser" la reine
		valeurInitiale = grille[x,y]
		# On remplit sur les lignes et les colonnes
		for i in range(tailleGrille):
			grille[x,i] = 1
			grille[i,y] = 1
		# Et maintenant les diagonales
		for k in range(tailleGrille):
			if (x+k < tailleGrille and y+k < tailleGrille and grille[x+k,y+k] != 2):
				grille[x+k,y+k] = 1
			if (x+k < tailleGrille and y-k > 0 and grille[x+k,y-k] != 2):
				grille[x+k,y-k] = 1
			if (x-k > 0 and y+k < tailleGrille and grille[x-k,y+k] != 2):
				grille[x-k,y+k] = 1
			if (x-k > 0 and y-k > 0 and grille[x-k,y-k] != 2):
				grille[x-k,y-k] = 1
		grille[reineActuelle] = valeurInitiale
	return(grille)


def calculEvaluation(solution,tailleGrille):
	grille = casesInterdites(solution,tailleGrille)
	evaluation = 0
	indiceReinesMalPlacees = []
	for k in range(len(solution)):
		valeurGrille = grille[solution[k]]
		if (valeurGrille != 0):
			evaluation += valeurGrille
			indiceReinesMalPlacees.append(k)
	return(int(evaluation),indiceReinesMalPlacees)

def voisin(solution,indiceReinesADeplacer,tailleGrille,temp):
	newSolution = copy.deepcopy(solution)
	for i in range(len(indiceReinesADeplacer)):
		#On s'assure de ne pas sortir de la grille, et qu'on ne tombe pas sur une case deja occupee
		caseOccupee = 1
		garantieSortie = 0
		compteurGarantie = 0
		indiceActuel = indiceReinesADeplacer[i]
		while(caseOccupee):
			caseOccupee = 0
			newX = min(tailleGrille-1,max(0,solution[indiceActuel][0] + random.randint(-(max(1,int(tailleGrille*temp))+garantieSortie),max(1,int(tailleGrille*temp))+garantieSortie)))
			#newY = min(tailleGrille-1,max(0,solution[indiceReinesADeplacer[i]][1] + random.randint(-(max(1,int(tailleGrille*temp))+garantieSortie),max(1,int(tailleGrille*temp))+garantieSortie)))
			newY = solution[indiceActuel][1]
			if (newX,newY) in newSolution:
				caseOccupee = 1
				compteurGarantie = compteurGarantie + 1
			if compteurGarantie == 10:
				garantieSortie = garantieSortie + 1
				compteurGarantie = 0
		newSolution[indiceActuel] = (newX,newY)
		#print("Indice deplace : " + str(indiceReinesADeplacer[i]))
		#print("Position initiale : " + str(solution[indiceActuel]))
		#print("Position deplacee : " + str(newSolution[i]))
	return(newSolution)


def affichage(solution,tailleGrille):
	for i in reversed(range(tailleGrille)):
		for j in range(tailleGrille):
			toPrint = "+"
			for k in range(len(solution)):
				if (i,j) == solution[k]:
					toPrint = str(k)
			print(toPrint+" ",end="")
		print("")
	
def nDames(n,tailleGrille, nombreIterations):
	solution = solutionInitiale(n,tailleGrille)
	nIter = 0
	evaluation = calculEvaluation(solution,tailleGrille)
	valeurEvaluation = evaluation[0]
	indiceReinesMalPlacees = evaluation[1]
	bestSolution = solution
	bestEvaluation = valeurEvaluation
	bestIterations = 0
	while (nIter < nombreIterations and valeurEvaluation != 0):
		temp = float(nombreIterations - nIter)/float(2*nombreIterations)
		nombreADeplacer = random.randint(1,len(indiceReinesMalPlacees))
		#nombreADeplacer = 1
		indicesADeplacer = []
		permutation = np.random.permutation(len(indiceReinesMalPlacees))
		for i in range(nombreADeplacer):
			indicesADeplacer.append(indiceReinesMalPlacees[permutation[i]])
		newSolution = voisin(solution,indicesADeplacer,tailleGrille,temp)
		newEvaluation = calculEvaluation(newSolution,tailleGrille)
		newValeurEvaluation = newEvaluation[0]
		newIndiceReinesMalPlacees = newEvaluation[1]
		
		#if (nIter % (nombreIterations/10) == 0):
		#	print("Iteration : " + str(nIter) + " || Evaluation : " + str(valeurEvaluation))

		'''
		print("Solution actuelle : ")
		affichage(solution,tailleGrille)
		print ("Evaluation solution : " + str(valeurEvaluation))
		print(str(nombreADeplacer) + " indices a deplacer : ")
		print(indicesADeplacer)
		print("Nouvelle solution : ")
		affichage(newSolution,tailleGrille)
		print("Nouvelle Evaluation : " + str(newValeurEvaluation))
		print("Temperature actuelle : "+ str(temp))
		'''
		
		testRecuit = random.random()	
		if (newValeurEvaluation < valeurEvaluation or testRecuit < math.exp(-abs(newValeurEvaluation - valeurEvaluation)/temp)):
			#print("On garde la nouvelle solution")
			valeurEvaluation = newValeurEvaluation
			indiceReinesMalPlacees = newIndiceReinesMalPlacees
			solution = newSolution
		#else:
			#print("On ne garde pas la nouvelle solution")
		nIter = nIter + 1
		#print("-------------------------")
		
		if (valeurEvaluation < bestEvaluation):
			bestEvaluation = valeurEvaluation
			bestSolution = copy.deepcopy(solution)
			bestIterations = nIter
	
	print("MEILLEURE SOLUTION TROUVEE (Nb de reines mal placees = " + str(bestEvaluation) +") en " + str(bestIterations) + " iterations" )
	print(bestSolution)
	affichage(bestSolution,tailleGrille)
	return(bestSolution)

nombreDames = int(sys.argv[1])
tailleGrille = int(sys.argv[2])
nombreIterations = int(sys.argv[3])

print(str(nombreDames) + " DAMES, ECHIQUIER TAILLE " + str(tailleGrille)+str("x")+str(tailleGrille)+ ", "+str(nombreIterations) + " ITERATIONS MAX")
nDames(nombreDames,tailleGrille,nombreIterations)





