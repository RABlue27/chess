# create a player vs player chess game using the chess library for play in the terminal
# December 2021
# Eduardo Saldana 6612626 and Alex Duclos 6738884
# Chess AI
import chess
import random
import math



# Maybe Final Heuristic
def heuristic(board):
    value = 0

    # first, identify checks and checkmates
    if board.is_checkmate():
        # if black is in checkmate, return a large value
        if board.turn == chess.WHITE:
            value = -100000
        else:
            value = 100000
    elif board.is_check():
        # if black is in check, return a large value
        if board.turn == chess.WHITE:
            value = -2
        else:
            value = 2

    for number in range(8):
        for letter in range(len("abcdefgh")):
            location = "abcdefgh"[letter]+str(number+1)
            piece = board.piece_at(chess.parse_square(location))
            if piece is not None:
                if piece.color == chess.WHITE:
                    if piece.piece_type == 1:  # Pawn
                        value += 1
                        value += WHITE_PAWN[7-number][letter]/10
                    elif piece.piece_type == 2: # Knight
                        value+=3  
                        value += WHITE_KNIGHT[7-number][letter]/10
                    elif piece.piece_type == 3: # Bishop
                        value+=3
                        value += WHITE_BISHOP[7-number][letter]/10
                    elif piece.piece_type == 4: # Rook
                         value+=5  
                         value += WHITE_ROOK[7-number][letter]/10
                    elif piece.piece_type == 5: # Queen
                        value+=9
                        value += WHITE_QUEEN[7-number][letter]/10
                    else: # King
                        value+=100
                        value += WHITE_KING[7-number][letter]/10
                else:  # If it's a black piece
                    if piece.piece_type == 1:  # Pawn
                        value -= 1
                        value -= BLACK_PAWN[7-number][letter]/10
                    elif piece.piece_type == 2: # Knight
                        value-=3  
                        value -= BLACK_KNIGHT[7-number][letter]/10
                    elif piece.piece_type == 3: # Bishop
                        value-=3
                        value -= BLACK_BISHOP[7-number][letter]/10
                    elif piece.piece_type == 4: # Rook
                         value-=5  
                         value -= BLACK_ROOK[7-number][letter]/10
                    elif piece.piece_type == 5: # Queen
                        value-=9
                        value -= BLACK_QUEEN[7-number][letter]/10
                    else: # King
                        value-=100 
                        value -= BLACK_KING[7-number][letter]/10

    return value

WHITE_PAWN =     [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [.75,  0.5,  1.0,  2.0,  2.0,  .50,  0.50,  0.75],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]
BLACK_PAWN = WHITE_PAWN[::-1]

WHITE_KNIGHT =     [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ]

BLACK_KNIGHT = WHITE_KNIGHT[::-1]

WHITE_BISHOP = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

BLACK_BISHOP = WHITE_BISHOP[::-1]

WHITE_ROOK = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]

BLACK_ROOK = WHITE_ROOK[::-1]

WHITE_QUEEN =  [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

BLACK_QUEEN = WHITE_QUEEN[::-1]

WHITE_KING = [
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]

BLACK_KING = WHITE_KING[::-1]




# alpha beta pruning minimax used to find and return the best move.
def minimax(board, depth, alpha, beta, maximizingPlayer):
    decision = None
    if depth == 0 or board.is_game_over():
        return heuristic(board), None
    if maximizingPlayer:
        max_value = float("-inf")
        for move in board.legal_moves:
            board.push(move)
            value = minimax(board, depth - 1, alpha, beta, False)[0]
            board.pop()
            if (value>max_value):
                max_value = value
                decision = move
            alpha = max(alpha, max_value)
            if beta <= alpha:
                break
        return max_value, decision
    else:
        min_value = float("inf")
        for move in board.legal_moves:
            board.push(move)
            value = minimax(board, depth - 1, alpha, beta, True)[0]
            board.pop()
            if (value<min_value):
                min_value = value
                decision = move
            beta = min(beta, min_value)
            if beta <= alpha:
                break
        return value, decision  


def pvp():
    # ask if user wants to paste in a board or use the default
    print("Do you want to paste in a board or use the default?")
    print("1. Paste in a board")
    print("2. Use the default")
    choice = input("Enter your choice: ")
    if choice == "1":
        board = chess.Board(input("Paste in your board: "))
    else:      
        board = chess.Board()

    # ask if user wants to output the board to a file or not
    print("Do you want to output the board to a file?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        output = open("output.txt", "w")
    else:
        output = None



    turn = 1

    while not board.is_game_over():
        print(board)
        print(board.legal_moves)
        print("\n")
        print("Player 1, please enter your move: ")
        move = input()
        board.push_san(move)
        print(board)
        print(board.legal_moves)
        print("\n")
        # print the move to the file if the user wants to
        if output != None:
            output.write(str(turn) + ". " + str(move))

        print("Player 2, please enter your move: ")
        move = input()
        board.push_san(move)
       # print the move to the file if the user wants to 
        if output != None:
            output.write(" " + str(move) + "\n")

        turn += 1

        print(board)
        print(board.legal_moves)
        print("\n")
    print(board)
    print(board.result())

def pvAI():
    # ask if user wants to paste in a board or use the default
    print("Do you want to paste in a board or use the default?")
    print("1. Paste in a board")
    print("2. Use the default")
    choice = input("Enter your choice: ")
    if choice == "1":
        board = chess.Board(input("Paste in your board: "))
    else:   
        board = chess.Board()   

    # ask if user wants to output the board to a file or not
    print("Do you want to output the board to a file?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        output = open("output.txt", "w")
    else:
        output = None

    print("Please enter the depth of the search: ")
    depth = int(input())

    turn = 1

    while not board.is_game_over():
        print(board)
        print(board.legal_moves)
        print("\n")
        print("Player 1, please enter your move: ")
        move = input()
        # print the move to the file if the user wants to
        if output != None:
            output.write(str(turn) + ". " + str(move))
        board.push_san(move)
        print(board)
        print(board.legal_moves)
        print("\n")
        
        # Use the minimax function to find the best move
        # for list of legal moves, try minimax
        # output best move to the board
        move = minimax(board,depth,-math.inf, math.inf,False)[1]
        print("Computer Played: "+str(move))
        # print the move to the file if the user wants to
        if output != None:
            output.write(" " + str(move) + "\n")

        board.push_san(str(move))
        print("\n")
        turn +=1 
        #legal_moves = list(board.legal_moves)
        
def AIvAI():
    # ask if user wants to paste in a board or use the default
    print("Do you want to paste in a board or use the default?")
    print("1. Paste in a board")
    print("2. Use the default")
    choice = input("Enter your choice: ")
    if choice == "1":
        board = chess.Board(input("Paste in your board: "))
    else:   
        board = chess.Board()   

    # ask if user wants to output the board to a file or not
    print("Do you want to output the board to a file?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        output = open("output.txt", "w")
    else:
        output = None

    print("Please enter the depth of the search: ")
    depth = int(input())

    turn = 1

    while not board.is_game_over():
        print(board)
        print("\n")
        move = minimax(board,depth,-math.inf, math.inf,True)[1]
        print("Computer 1 Played: "+str(move))
        # print the move to the file if the user wants to
        if output != None:
            output.write(str(turn) + ". " + str(move))

        board.push_san(str(move))

        print(board)
        print("\n")
        # select a random legal move
        if (len(list(board.legal_moves)) > 0):
            move = random.choice(list(board.legal_moves))
            # print the move to the file if the user wants to
            if output != None:
                output.write(" " + str(move) + "\n")

        

        else: 
            print("No legal moves")
            break
        
        turn +=1 

        print("Computer 2 Played: "+str(move))
        board.push_san(str(move))
    
        #print(heuristic(board))

    print(board.result())


# start the main gameloop
def main():
    # ask the user if they want to play against the computer or another player
    print("Welcome to chess!\n")
    print("Would you like to play against the computer or another player?")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    print("3. Computer vs Computer")
    print("4. Quit")
    choice = input("Enter your choice: ")
    # if the user chooses to play against another player
    if choice == "1":
        pvp()
    if choice == "2":
        pvAI()
    if choice == "3":
        AIvAI()
    else:
        print("Goodbye!")
        exit()
    main()

main()
