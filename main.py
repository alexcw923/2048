from utilities import place_random, print_board
DEV_MODE = False
def one_line(game_board):
    tracker = False
    for col in range(len(game_board)):
        prev = game_board[col]
        if prev == 0:
            pass
        else:
            for i in range(col + 1, len(game_board)):
                if prev == game_board[i]:
                    tracker = True
                    game_board[col] *= 2
                    game_board[i] = 0
                    break
                elif game_board[i] != 0:
                    break
    if 0 not in game_board:
        return tracker
    for col in range(len(game_board)):
        if game_board[col] != 0 and game_board.index(0) < col:
            tracker = True
    for col in range(len(game_board)):
        if game_board[col] == 0:
            game_board.remove(game_board[col])
            game_board.append(0)
    return tracker
def up(game_board):
    check = 0
    for col in range(4):
        ls = []
        for row in range(4):
            ls.append(game_board[row][col])
        if one_line(ls):
            check += 1 
        for row in range(4):
            game_board[row][col] = ls[row]
    if check > 0:
        return True
    else:
        return False 
def left(game_board):
    check = 0
    for row in range(len(game_board)):
        if one_line(game_board[row]):
            check += 1
    if check > 0:
        return True
    else:
        return False                
def down(game_board):
    check = 0
    for col in range(4):
        ls = []
        for row in range(4):
            ls.append(game_board[row][col])
        ls.reverse()
        if one_line(ls):
            check += 1
        ls.reverse()
        for row in range(4):
            game_board[row][col] = ls[row]
    if check > 0:
        return True
    else:
        return False 
def right(game_board):
    check = 0
    for row in range(len(game_board)):
        game_board[row].reverse()
        if one_line(game_board[row]):
            check += 1
        game_board[row].reverse()
    if check > 0:
        return True
    else:
        return False
def win(game_board: [[int, ], ]) -> bool:
    for row in game_board:
        for column in row:
            if column == 2048:
                return True
    return False
def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # You are not required to implement develop mode, but it is encouraged to do so.
    # Develop mode allows you to input the location of the next piece that will be
    # placed on the board, rather than attempting to debug your code with random
    # input values.
    if DEV_MODE:
        # This line of code handles the input of the develop mode.
        column, row, value = (int(i) for i in input("column,row,value:").split(','))
         # OPTIONAL: place the piece in the corresponding cell on the game board
    else:
        # TODO: generate a random piece and location using the place_random function
        game_dict = place_random(game_board)
        game_board[game_dict['row']][game_dict['column']] = game_dict['value']
        # TODO: place the piece at the specified location

    # Initialize game state trackers
    flag = True

    # Game Loop
    while flag:
        # TODO: Reset user input variable
        # TODO: Take computer's turn
        # place a random piece on the board
        # check to see if the game is over using the game_over function
        game_dict = place_random(game_board)
        game_board[game_dict['row']][game_dict['column']] = game_dict['value']
        # TODO: Show updated board using the print_board function
        print_board(game_board)
        if game_over(game_board):
            print('Game Over')
            break
        # TODO: Take user's turn
        # Take input until the user's move is a valid key
        # if the user quits the game, print Goodbye and stop the Game Loop
        # Execute the user's move
        control = True
        while control:
            control = True
            player_move = input('enter:')
            if player_move not in ('w', 'a', 's', 'd', 'q'):
                pass
            if player_move == 'q':
                print('Goodbye')
                flag = False
                break
            elif player_move == 'w':
                control = not up(game_board)
            elif player_move == 'a':
                control = not left(game_board) #True run again
            elif player_move == 's':
                control = not down(game_board)
            elif player_move == 'd':
                control = not right(game_board)
        # Check if the user wins
        if win(game_board):
            print('You Win')
            break
    return game_board
def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    for row in game_board:
        if 0 in row:
            return False
    for row in range(4):
        for col in range(4):
            if row != 0 and game_board[row][col] == game_board[row - 1][col]:
                return False
            if row != 3 and game_board[row][col] == game_board[row + 1][col]:
                return False
            if col != 0 and game_board[row][col] == game_board[row][col - 1]: 
                return False
            if col != 3 and game_board[row][col] == game_board[row][col + 1]:
                return False
    return True  # TODO: Don't always return false


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])