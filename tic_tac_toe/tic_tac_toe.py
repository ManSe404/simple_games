from tic_tac_toe import tic_tac_toe_funcs

# ------------------ Global variables  -------------------
GAME_ON = True
SPACE_INDEX = ['zero_index', '1', '2', '3', '4', '5', '6', '7', '8', '9']
WINNER = None


# GAME LOGIC
def play_again():
    answer = ""
    while answer != "Y" or answer != "N":
        answer = input("Do you want to play again (Y or N): ").upper()
        if answer == "Y":
            return tic_tac_toe_game()
        elif answer == "N":
            break


def tic_tac_toe_game():

    print("Welcome to Tic Tac Toe")
    tic_tac_toe_funcs.display_board(SPACE_INDEX)

    empty_board = tic_tac_toe_funcs.empty_list()
    tic_tac_toe_funcs.display_board(empty_board)
    updated_board = empty_board

    current_player = tic_tac_toe_funcs.starting_player()

    while GAME_ON:

        # PLAYER ACTION ON THE BOARD
        updated_board = tic_tac_toe_funcs.action_input(updated_board, current_player)
        tic_tac_toe_funcs.display_board(updated_board)

        # CHECKS FOR WIN,TIE AND AVAILABLE PLACE
        game_over_check = tic_tac_toe_funcs.check_game_over(updated_board, current_player)
        if game_over_check is True:
            break

        current_player = tic_tac_toe_funcs.filter_between_players(current_player)

    play_again()
