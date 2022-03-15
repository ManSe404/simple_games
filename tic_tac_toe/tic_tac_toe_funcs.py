# Create an empty list as representation of places on the board to manipulate
def empty_list():
    board_list = ["-"] * 10
    return board_list


# Display board
def display_board(space):

    print('   |   |')
    print(' ' + space[7] + ' | ' + space[8] + ' | ' + space[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + space[4] + ' | ' + space[5] + ' | ' + space[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + space[1] + ' | ' + space[2] + ' | ' + space[3])
    print('   |   |')


# Check if space is empty for marker to be put
def check_space(space):
    if space == "X" or space == "O":
        return True
    else:
        return False


# Player makes an action on board
def action_input(space, current_player):
    acceptable_range = range(1, 10)
    action = input("Please pick a place for marker: ")
    while action.isdigit() is False or int(action) not in acceptable_range or check_space(space[int(action)]) is True:
        action = input("Please pick a place for marker: ")

    space[int(action)] = current_player
    return space


def check_game_over(current_board, player_mark):

    win_check = check_if_win(current_board, player_mark)
    draw_check = check_if_draw(current_board)

    if win_check is True:
        print(f"{player_mark} wins")
        return True

    elif draw_check is True:
        print("IT IS A TIE")
        return True

    else:
        return False


# CHECK FOR WIN
def check_if_win(current_board, current_player_mark):
    return ((current_board[7] == current_board[8] == current_board[9] == current_player_mark) or  # top win
            (current_board[4] == current_board[5] == current_board[6] == current_player_mark) or  # middle win
            (current_board[1] == current_board[2] == current_board[3] == current_player_mark) or  # bottom win
            (current_board[7] == current_board[4] == current_board[1] == current_player_mark) or  # down the left
            (current_board[8] == current_board[5] == current_board[2] == current_player_mark) or  # down the middle
            (current_board[9] == current_board[6] == current_board[3] == current_player_mark) or  # down the right
            (current_board[7] == current_board[5] == current_board[3] == current_player_mark) or  # diagonal
            (current_board[9] == current_board[5] == current_board[1] == current_player_mark))  # diagonal


# CHECK FOR TIE
def check_if_draw(current_board):
    check_board = current_board[1:10]
    if "-" not in check_board:
        return True


# Define starting player
def starting_player():
    return 'X'


# Player turn filter
def filter_between_players(player):
    if player == "X":
        return "O"
    return 'X'
