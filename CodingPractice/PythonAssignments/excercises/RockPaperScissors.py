
def player_1_rock(player_2):
    player_2 = player_2.lower()
    if player_2 == 'paper':
        return False
    elif player_2 == 'scissors':
        return True
    else:
        return None


def player_1_paper(player_2):
    player_2 = player_2.lower()
    if player_2 == 'scissors':
        return False
    elif player_2 == 'rock':
        return True
    else:
        return None


def player_1_scissors(player_2):
    player_2 = player_2.lower()
    if player_2 == 'rock':
        return False
    elif player_2 == 'paper':
        return True
    else:
        return None


def is_valid_input(player_1, player_2):
    return player_1 in {'rock', 'paper', 'scissors'} \
           and player_2 in {'rock', 'paper', 'scissors'}


def rock_paper_scissors(player_1, player_2):
    if player_1 == 'rock':
        return player_1_rock(player_2)

    elif player_1 == 'scissors':
        return player_1_scissors(player_2)

    elif player_1 == 'paper':
        return player_1_paper(player_2)

    else:
        return "Invalid input."

