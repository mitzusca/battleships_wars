from random import randint

your_board = []
your_guesses_board = []
computer_board = []


def create_board(board):
    """
    Creating a board from 7 lists wich hold question marks
    """
    for a in range(7):
        board.append([' ? ']*7)
    return board


def print_board(board):
    """
    Print the board and remove quotes, commas and brackets
    """
    for ind in board:
        print(" ".join(ind))


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
        board[ship_x][ship_y] = " @ "
        for x in board:
            ship_num += x.count(" @ ")


def welcome_message():
    """
    Welcome message that explains the game idea and ask for a nickname
    """
    print("Welcome to Warships Battle!")
    nickname = input('Type your nickname and press enter: \n')
    print(f'\nHello {nickname}!\n')
    print('There are hidden 6 ship\'s under computer map')
    print('Using numbers between 1 and 7')
    print('Discover all ship\'s to destroy them')
    print('\n? are undiscovered locations')
    print('X represent a HIT! ')
    print('O represents a MISS!')


def create_boards():
    """
    Calling functions to create boards and ships for player and computer
    """

    create_board(computer_board)
    create_board(your_board)
    create_board(your_guesses_board)
    create_ship(your_board)
    create_ship(computer_board)


def your_guesses():
    """
    Add method for guessing location to change it acordingly
    and validate if inputs are integers between 1 and 7
    """
    print_board(your_guesses_board)
    repeat = True
    while repeat:
        while True:
            chosen_column = input('\nChoose the Column:')
            if validate_data(chosen_column):
                break
        while True:
            chosen_row = input('Choose the Row:')
            if validate_data(chosen_row):
                break
        print(f'\nYou have chosen column {chosen_column}/ row {chosen_row}')
        chosen_column = int(chosen_column)-1
        chosen_row = int(chosen_row)-1
        # int -1 because python begins with 0 and we want to use
        # numbers between 1 and 7
        if (your_guesses_board[chosen_row][chosen_column] == " O " or
                your_guesses_board[chosen_row][chosen_column] == " X "):
            print('This time try a new spot!')
        else:
            repeat = False
    if computer_board[chosen_row][chosen_column] == " @ ":
        your_guesses_board[chosen_row][chosen_column] = " X "
        print("Bravo, you hit him!\n")
    else:
        your_guesses_board[chosen_row][chosen_column] = " O "
        print('Unfortunately you missed!\n')


def computer_guesses():
    """
    Computer guess at user board using randomly generate coordinates
    """
    repeat = True
    chosen_column = random_num(computer_board)
    chosen_row = random_num(computer_board)
    while repeat:
        if (your_board[chosen_row][chosen_column] ==
            " O " or your_board[chosen_row][chosen_column] ==
                " X "):
            chosen_column = random_num(computer_board)
            chosen_row = random_num(computer_board)
        else:
            repeat = False
    print(f'Computer choose column {chosen_column + 1}/ row {chosen_row + 1}')
    if your_board[chosen_row][chosen_column] == " @ ":
        your_board[chosen_row][chosen_column] = " X "
        print('Computer hit you!')
    else:
        your_board[chosen_row][chosen_column] = " O "
        print('Computer missed you!')


def new_game():
    """
    The main loop to generate a new game and play the game
    """
    create_boards()
    welcome_message()
    i = 0
    while i < 30:
        input("\nPress Enter to continue...")
        print(f'\nThis is turn {i+1} from 30 ')
        print('\nThis is your board!')
        print_board(your_board)
        print(' ')
        print("-" * 35)
        print('\nThis is the computer board!')
        your_guesses()
        computer_guesses()
        i += 1
        if check_winner(your_board) == 6:
            i = 30
        elif check_winner(your_guesses_board) == 6:
            i = 30
    check_winner_final()


def validate_data(value):
    """
    If value is not an integer between 1 and 7 and, it raise an error
    and request a new value
    """
    try:
        if int(value) > 7 or int(value) < 1:
            raise ValueError
    except ValueError as e:
            print('Invalid value!')
            print('Values must be numbers betwen 1 and 7!\n')
            return False
    return True


def check_winner(board):
    """
    Sums the number of times " X "  appear in the board.
    """
    total = 0
    for list in board:
        total += list.count(" X ")
    return total


def check_winner_final():
    """
    Check for a winner after 30 turns and report the result to the user
    """
    your_result = check_winner(your_guesses_board)
    computer_result = check_winner(your_board)
    if your_result > computer_result:
        print("Congratulations! You WIN!")
    elif your_result < computer_result:
        print("\nToo bad! - the computer had the most hits!")
    else:
        print("\nIt was a draw!")
new_game()