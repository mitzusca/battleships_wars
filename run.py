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


def print_board(board):
    """
    Print the board and remove quotes, commas and brackets  
    """
    for ind in board:
        print("~".join(ind))


def random_num(board):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, len(board)-1)


def create_ship(board):
    """
    Create 6 random ships on board.
    """
    ship_num = 0
    while ship_num < 6:
        ship_num = 0
        ship_x = random_num(board)
        ship_y = random_num(board)
        board[ship_x][ship_y] = "X"
        for x in board:
            ship_num += x.count("X")


def create_boards():
    """
    Creating boards and ships for you and computer
    """
    create_board(your_board)
    create_board(computer_board)
    create_board(your_guesses_board)

print(create_boards())   
