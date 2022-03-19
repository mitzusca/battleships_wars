from random import randint 

your_board = []
your_guesses_board = []
computer_board = []

def create_board(board):
    """
    Creating a board from 7 lists wich hold question marks
    """
    for a in range(7):
        board.append(['?'*7])
    return board
b = create_board(your_board)
print(b)
def random_num(board):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, len(board)-1)
