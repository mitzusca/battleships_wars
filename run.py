from random import randint 

your_board = []
your_guesses_board = []
computer_board = []


def create_board(board):
    """
    Creating a board from 7 lists wich hold question marks
    """
    for a in range(7):
        board.append([' ? '*7])
    return board


c = create_board(your_board)


def print_board(board):
    """
    Print the board and remove quotes, commas and brackets    
    """
    for ind in board:
        print("".join(ind))


print_board(c)


def random_num(board):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, len(board)-1)
