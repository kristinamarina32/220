"""
Name: Kristina Rydbom
lab10.py

Problem: Lab 10 problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def create_board():
    # creating the board
    # A method to build the board.  This method should create a list of numbers 1 – 9 and return that list.
    num_list =[1,2,3,4,5,6,7,8,9]
    return num_list
    # print(*data, sep='') to separate them without commas or brackets


def draw_board(board):
    #  A void method to display the board.
    counter = 0
    for i in range(3):
        print(board[counter], "|", board[counter + 1], "|", board[counter + 2])
        print("---------")
        counter += 3


def mark_space(board, position, character):
    #   A void method to fill a spot on the board.
    #   This method will need to have the board, the position to be filled and the character to place in that position.
    #   Do some error checking here so that the board does not allow for letters other than ‘x’ and ‘o’.
    new = character.upper()
    if (new == "X" or new == "O") and (valid_move(board, position)):
        board[position - 1] = new


def valid_move(board, position):
    # A Boolean method to determine if a spot is a legal spot on the board.
    # Don’t allow the method mentioned in the previous bullet to execute if the spot isn’t legit.
    if str(board[position - 1]).isnumeric():
        return True
    return False


def game_won(board):
    # A Boolean method to determine if the game has been won.
    # X
    if board[0:3] == ["X","X","X"] or board[3:6] == ["X","X","X"] or board[6:] == ["X","X","X"]:
        print("X has won!")
        return True
    if board[0::4] == ["X","X","X"] or board[2::2] == ["X","X","X"]:
        print("X has won!")
        return True
    if board[0::3] == ["X","X","X"] or board[1::3] == ["X","X","X"] or board[2::3] == ["X","X","X"]:
        print("X has won!")
        return True
    # O
    if board[0:3] == ["O","O","O"] or board[3:6] == ["O","O","O"] or board[6:] == ["O","O","O"]:
        print("O has won!")
        return True
    if board[0::4] == ["O","O","O"] or board[2::2] == ["O","O","O"]:
        print("O has won!")
        return True
    if board[0::3] == ["O","O","O"] or board[1::3] == ["O","O","O"] or board[2::3] == ["O","O","O"]:
        print("O has won!")
        return True


def game_over(board):
    # A Boolean method to determine if the game is over.
    # This should call the previously mentioned method
    # plus check to make sure there are more plays allowed on the board.
    if game_won(board):
        return True
    for i in board:
        if str(i).isnumeric():
            return False
    return True


def play_game(board):
    # A method to play the game.  This method should continue as long as the game is not over.
    # Once the game is over, display the message “Player 1 wins!”, “Player 2 wins”, or “Tie” as appropriate.
    print("Tic-Tac-Toe Game")
    print("For each move, enter either X or O as your character and then enter the position you want it to be placed")
    create_board()
    while not(game_over(board)):
        draw_board(board)



def main():
    # add other function calls here
    create_board()
    board = create_board()
    draw_board(board)
    mark_space(board, position, character)
    valid_move(board, position)
    game_won(board)
    game_over(board)

    pass


main()
