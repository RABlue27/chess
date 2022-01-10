Introduction
============
This program uses the ['chess'](https://github.com/niklasf/python-chess) library to play chess.

This program requres python 3.10 or higher. Failure to meet these requirements will result in an error importing the library. 

To install this library, assuming you have pip installed, run the following command:
pip install chess



To play a game of chess, simply run the program. A prompt will ask which variation of the program would you like to run, and then the program will run the game.

The option are:
Player vs Player
Player vs Computer (This uses the minimax algorithm)
Computer vs Computer (This uses the minimax algorithm played against a computer making random moves)

Further options are depth of the tree. A depth of 5 is suggested on modern computers, but a depth of 4 or 3 would be fine on older computers.

Custom board formats use the ['FEN'](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) notation. Simply enter the FEN notation in the prompt. Do not enter as a string. 

Output to a file is also supported. The file will be named 'output.txt' and will be saved in the same directory as the program. 

