def grid(grid_: list[list[int]]):
    """
    Display the grid in the console by replacing the value of the player by their symbol

    :param grid_: The grid of the current game
    """
    grid_appearance: str = "- " * 5 + "\n"
    for line in grid_:
        line_appearance: str = ""
        for cell in line:
            if cell == 0:
                line_appearance += "X | "
            elif cell == 1:
                line_appearance += "  | "
            elif cell == 2:
                line_appearance += "O | "
        grid_appearance += line_appearance[:-2] + "\n" + "- " * 5 + "\n"
    print(grid_appearance)


def winner(grid_: list[list[int]], winner_: int, turn: int):
    """
    Display the winner of the game and the last grid

    :param grid_: The grid of the current game
    :param winner_: The winner of the current game
    :param turn: The number of turn during the game
    """
    print("--- Fin de la partie ---\n")
    if winner_ == 0:
        print(f"La partie se termine par la victoire du joueur en {turn} tours")
    elif winner_ == 1:
        print(f"La partie se termine par une égalité en {turn} tours")
    else:
        print(f"La partie se termine par la victoire de l'ordinateur en {turn} tours")
    print()
    grid(grid_)
