from tic_tac_toe import tic_tac_toe as tt


def pick_a_game():

    print("LIST OF GAMES: 1) TIC TAC TOE")
    acceptable_picks = [1]
    pick = input("Please pick a game number: ")

    while pick.isdigit() is False or int(pick) not in acceptable_picks:
        pick = input("Please pick a game number: ")

    pick = int(pick)
    return pick


if __name__ == "__main__":

    print("PICK A GAME TO FROM THE LIST TO PLAY")
    game = pick_a_game()
    if game == 1:
        tt.tic_tac_toe_game()
