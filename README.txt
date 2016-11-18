This program was coded using Python 2.7, and you will need numPy for it to compile.
It solves the 8 queens puzzle, generalized to any number of queen. For more information, you can look up the wikipedia page : https://en.wikipedia.org/wiki/Eight_queens_puzzle


The calling syntax is the following : 

	python nQueens.py nb_Queens chessboard_size nbIterations


With
	- nb_Queens the number of queens you want to place on the chessboard
	- chessboard_size the width and length of the chessboard (the puzzle is usually solved with this value equal to the number of queens)
	- nbIterations, the max allowed number of iterations

As this program uses a simulated anneling method, it depends upon the temperature of the algorithm, temperature which depends on the numer of iterations. So the more iterations you allow, the more likely the program is to find a correct solution, but the slower it is.

It is possible the program won't find a correct solution because of the randomisation in the algorithm. I encourage you to lauch the program again in this case, it will eventually find a solution. Maybe you didn't but enough iterations ?


As an output, the program firstly displays the parameters provided, then the best solution it found, with the number of queens it couldn't place correctly if it didn't find a correct solution, and the number of iterations it took for it to find this solution.
It then provides the (x,y) coordinates of each queen, and displays them on a grid.


If you want to use this program in one of your project, go ahead ! To get the array of the solution, you just need to import the py and call the function

	nQueens(nb_Queens,chessboard_size, nbIterations)