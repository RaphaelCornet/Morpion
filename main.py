from game import Game

current_identifier: int = 0


def morpion():
    """
    The main function of this project
    """
    while True:
        game()


def game():
    global current_identifier
    current_identifier += 1
    Game(current_identifier).start()


if __name__ == '__main__':
    morpion()
