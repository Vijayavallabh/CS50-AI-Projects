"""
Tic Tac Toe Player
"""

import math
import random
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0
    count_e = 0
    if terminal(board):
        return None
    for i in board:
        for j in i:
            if j == O:
                count_o +=1
            elif j == X:
                count_x +=1
            else:
                count_e+=1
    if count_e>0:
        if count_x > count_o:
            return O
        elif count_o >= count_x:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleactions = set()

    # game is over
    if terminal(board):
        return None

    # game is not over, add all possible actions to the set
    for iIndex, i in enumerate(board):  # row
        for jIndex, j in enumerate(i):  # column
            if j == EMPTY:              # Add the index of the empty cell to the set
                possibleactions.add((iIndex, jIndex))

    return possibleactions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    currentPlayer = player(board)
    boardClone = copy.deepcopy(board)

    # check if the range action is within 0 to 2, raise ValueError if not
    for selectedIndex in action:
        if selectedIndex > 2 or selectedIndex < 0:
            raise ValueError("Invalid action")

    # raise ValueError if the cell is not empty
    if boardClone[action[0]][action[1]] != EMPTY:
        raise Exception("Cell already occupied")

    # Set the cell to the current player
    else:
        boardClone[action[0]][action[1]] = currentPlayer

    return boardClone




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0, len(board)):
       
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != EMPTY):
            return board[i][0]

        
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != EMPTY):
            return board[0][i]

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != EMPTY):
        return board[0][0]
    
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != EMPTY):
        return board[0][2]

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    roundResult = winner(board)
    if roundResult is not None:
        return True

  
    for i in board:
        for j in i:
            if j == EMPTY:
                return False

    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winPlayer = winner(board)

    if winPlayer == X:
        return 1
    elif winPlayer == O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    The minimax algorithm, max_value and min_value are based on the pseudocode in the lecture 0.
    """
    currentPlayer = player(board)
    optimalAction = []


    if board == initial_state():
        optimalAction = (random.randint(0, 2), random.randint(0, 2))
        return optimalAction

  
    if terminal(board):
        return None

  
    else:
     
        if currentPlayer == X:
            possibleActions = actions(board)
            currentBestValue = -math.inf

            for action in possibleActions:
                
                value = min_value(result(board, action))
                
                if value > currentBestValue:
                    currentBestValue = value
                    optimalAction = action

            return optimalAction

   
        else:
            possibleActions = actions(board)
            currentBestValue = math.inf

            for action in possibleActions:
            
                value = max_value(result(board, action))
             
                if value < currentBestValue:
                    currentBestValue = value
                    optimalAction = action

            return optimalAction


def max_value(board):

    value = -math.inf

    if terminal(board):
        return utility(board)

   
    else:
        for action in actions(board):
            value = max(value, min_value(result(board, action)))
        return value


def min_value(board):

    value = math.inf

 
    if terminal(board):
        return utility(board)

 
    else:
        for action in actions(board):
            value = min(value, max_value(result(board, action)))
        return value

