def d_grid(grid: list[list[int]]):
    grid_appearance: str = "- " * 5 + "\n"
    for line in grid:
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


def d_winner(grid: list[list[int]], winner: int, turn: int):
    print("--- Fin de la partie ---\n")
    if winner == 0:
        print(f"La partie se termine par la victoire du joueur en {turn} tours")
    elif winner == 1:
        print(f"La partie se termine par une égalité en {turn} tours")
    else:
        print(f"La partie se termine par la victoire de l'ordinateur en {turn} tours")
    print()
    d_grid(grid)
