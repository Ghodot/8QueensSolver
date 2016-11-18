from __future__ import print_function

import numpy as np
import random
import copy
import math
import sys



def initialize_grid(chessboard_size):
	grid = np.zeros((chessboard_size,chessboard_size))
	return(grid)

def initial_solution(nb_Queens,chessboard_size):
	sol = np.zeros((nb_Queens,chessboard_size,chessboard_size))
	arrayQueens = []
	for i in range(nb_Queens):
		arrayQueens.append((i,i))
	return(arrayQueens)

#On place des 1 aux endroits interdits
def forbidden_squares(reines,chessboard_size):
	grid = initialize_grid(chessboard_size)
	for considered_queen in reines:
		x = considered_queen[0]
		y = considered_queen[1]
		# On memorise la valeur de la case avant de "poser" la reine
		initial_value = grid[x,y]
		# On remplit sur les lignes et les colonnes
		for i in range(chessboard_size):
			grid[x,i] = 1
			grid[i,y] = 1
		# Et maintenant les diagonales
		for k in range(chessboard_size):
			if (x+k < chessboard_size and y+k < chessboard_size and grid[x+k,y+k] != 2):
				grid[x+k,y+k] = 1
			if (x+k < chessboard_size and y-k > 0 and grid[x+k,y-k] != 2):
				grid[x+k,y-k] = 1
			if (x-k > 0 and y+k < chessboard_size and grid[x-k,y+k] != 2):
				grid[x-k,y+k] = 1
			if (x-k > 0 and y-k > 0 and grid[x-k,y-k] != 2):
				grid[x-k,y-k] = 1
		grid[considered_queen] = initial_value
	return(grid)


def evaluation_computing(solution,chessboard_size):
	grid = forbidden_squares(solution,chessboard_size)
	evaluation = 0
	subscript_incorrect_queens = []
	for k in range(len(solution)):
		grid_value = grid[solution[k]]
		if (grid_value != 0):
			evaluation += grid_value
			subscript_incorrect_queens.append(k)
	return(int(evaluation),subscript_incorrect_queens)

def voisin(solution,subscript_queens_to_be_moved,chessboard_size,temp):
	newSolution = copy.deepcopy(solution)
	for i in range(len(subscript_queens_to_be_moved)):
		#On s'assure de ne pas sortir de la grid, et qu'on ne tombe pas sur une case deja occupee
		square_occupied = 1
		exit_guarrantee = 0
		guarrantee_counter = 0
		subscript_considered = subscript_queens_to_be_moved[i]
		while(square_occupied):
			square_occupied = 0
			newX = min(chessboard_size-1,max(0,solution[subscript_considered][0] + random.randint(-(max(1,int(chessboard_size*temp))+exit_guarrantee),max(1,int(chessboard_size*temp))+exit_guarrantee)))
			#newY = min(chessboard_size-1,max(0,solution[subscript_queens_to_be_moved[i]][1] + random.randint(-(max(1,int(chessboard_size*temp))+exit_guarrantee),max(1,int(chessboard_size*temp))+exit_guarrantee)))
			newY = solution[subscript_considered][1]
			if (newX,newY) in newSolution:
				square_occupied = 1
				guarrantee_counter = guarrantee_counter + 1
			if guarrantee_counter == 10:
				exit_guarrantee = exit_guarrantee + 1
				guarrantee_counter = 0
		newSolution[subscript_considered] = (newX,newY)
		#print("Indice deplace : " + str(subscript_queens_to_be_moved[i]))
		#print("Position initiale : " + str(solution[subscript_considered]))
		#print("Position deplacee : " + str(newSolution[i]))
	return(newSolution)


def affichage(solution,chessboard_size):
	for i in reversed(range(chessboard_size)):
		for j in range(chessboard_size):
			toPrint = "+"
			for k in range(len(solution)):
				if (i,j) == solution[k]:
					toPrint = str(k)
			print(toPrint+" ",end="")
		print("")
	
def nQueens(nb_Queens,chessboard_size, nbIterations):
	solution = initial_solution(nb_Queens,chessboard_size)
	nIter = 0
	evaluation = evaluation_computing(solution,chessboard_size)
	evaluation_value = evaluation[0]
	subscript_incorrect_queens = evaluation[1]
	bestSolution = solution
	bestEvaluation = evaluation_value
	bestIterations = 0
	while (nIter < nbIterations and evaluation_value != 0):
		temp = float(nbIterations - nIter)/float(2*nbIterations)
		number_to_move = random.randint(1,len(subscript_incorrect_queens))
		#number_to_move = 1
		subscript_to_move = []
		permutation = np.random.permutation(len(subscript_incorrect_queens))
		for i in range(number_to_move):
			subscript_to_move.append(subscript_incorrect_queens[permutation[i]])
		newSolution = voisin(solution,subscript_to_move,chessboard_size,temp)
		newEvaluation = evaluation_computing(newSolution,chessboard_size)
		new_evaluation_value = newEvaluation[0]
		new_subscript_incorrect_queens = newEvaluation[1]
		
		
		simulated_annealing_random = random.random()	
		if (new_evaluation_value < evaluation_value or simulated_annealing_random < math.exp(-abs(new_evaluation_value - evaluation_value)/temp)):
			evaluation_value = new_evaluation_value
			subscript_incorrect_queens = new_subscript_incorrect_queens
			solution = newSolution

		nIter = nIter + 1

		
		if (evaluation_value < bestEvaluation):
			bestEvaluation = evaluation_value
			bestSolution = copy.deepcopy(solution)
			bestIterations = nIter
	
	if(bestEvaluation == 0):
		print("A SOLUTION WAS FOUND in " + str(bestIterations) + " iterations" )
	else:
		print("BEST FOUND SOLUTION ( "+str(bestEvaluation) +" queen(s) couldn't be placed correctly ) in " + str(bestIterations) + " iterations" )
	print(bestSolution)
	affichage(bestSolution,chessboard_size)
	return(bestSolution)

numberQueens = int(sys.argv[1])
chessboard_size = int(sys.argv[2])
nbIterations = int(sys.argv[3])

print("\n")
print(str(numberQueens) + " queens to place, chessboard size : " + str(chessboard_size)+str("x")+str(chessboard_size)+ ", "+str(nbIterations) + " iterations allowed")
nQueens(numberQueens,chessboard_size,nbIterations)





