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
    adding "~" as waves
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
        board[ship_x][ship_y] = " @ "
        for x in board:
            ship_num += x.count(" @ ")


def welcome_message():
    """
    Welcome message that explains the game idea and ask for a nickname
    """
    print("Welcome to Warships Battle!")
    nickname = input('Type your nickname and press enter: \n')
    print(f'\nHello {nickname}! Help us to destroy all')
    print('6 ships that belongs to computer')
    print('? are undiscovered locations, X represents a HIT!')
    print('and O represents a MISS!')
    print('Use numbers between 1 and 7 to locate them on the row and column.')


def create_boards():
    """
    Calling to create boards and ships for you and computer
    """
    create_board(your_board)
    create_board(computer_board)
    create_board(your_guesses_board)
    create_ship(your_board)
    create_ship(computer_board)


def your_guesses():
    """
    Add method for guessing location to change it acordingly
    and validate if inputs are integers between 1 and 7
    """
    print('This is the computer board!')
    print_board(your_guesses_board)
    repeat = True
    while repeat:
        while True:
            chosen_column = input('Choose the Column: \n')
            if validate_data(chosen_column):
                break
        while True:
            chosen_row = input('Choose the Row: \n')
            if validate_data(chosen_row):
                break
        chosen_column = int(chosen_column)-1
        chosen_row = int(chosen_row)-1
        # int -1 because python begins with 0 and it will
        # be used numbers between 1 and 7
        if (your_guesses_board[chosen_row][chosen_column] == " O " or
                your_guesses_board[chosen_row][chosen_column] == " X "):
            print('This time try a new spot!')
        else:
            repeat = False
    if computer_board[chosen_row][chosen_column] == " @ ":
        your_guesses_board[chosen_row][chosen_column] = " X "
        print("\n Bravo, you hit him! ")
    else:
        your_guesses_board[chosen_row][chosen_column] = " O "
        print('\n Unfortunately you missed!')


def computer_guesses():
    """
    Computer guess at user board using randomly generate coordinates
    """
    print('\n Computer turn!')
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
    print(f'Computer choosed {chosen_row + 1},{chosen_column + 1}')
    if your_board[chosen_row][chosen_column] == " @ ":
        your_board[chosen_row][chosen_column] = " X "
        print('Computer hit you!')
    else:
        your_board[chosen_row][chosen_column] = " O "
        print('Super, he missed!')


def new_game():
    """
    The main loop to generate a new game
    """
    create_boards()
    welcome_message()
    i = 0
    while i < 30:
        print(f'This is turn {i+1}/30 \n')
        your_guesses()
        print_board(your_guesses_board)
        input("\nPress Enter to continue...")
        computer_guesses()
        print('Your board:')
        print_board(your_board)
        input("\nPress Enter to continue...")
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
            raise ValueError('Please choose an number between 1 and 7!')
    except ValueError as e:
            print(f'Invalid data {e}, please try again.')
            print('Choose an number between 1 and 7.')
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
        print("Too bad! - the computer had the most hits!")
    else:
        print("It was a draw!")
new_game()