from random import randint 

def random_num(board):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, len(board)-1)
