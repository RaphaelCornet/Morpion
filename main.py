from typing import Optional

from display import d_grid, d_winner
from grid import create, finish
from player import computer_turn, human_turn, random


def main():
    grid: list[list[int]] = create()
    starter: int = random()
    turn: int = 0
    result: tuple[bool, Optional[int]] = False, None
    while not result[0]:
        turn += 1
        print(f"--- Tour n°{turn} ---\n")
        if starter == 0:
            d_grid(grid)
            human_turn(grid)
            result = finish(grid)
            if result[0]:
                break
            computer_turn(grid)
        elif starter == 2:
            computer_turn(grid)
            result = finish(grid)
            if result[0]:
                break
            d_grid(grid)
            human_turn(grid)
        result = finish(grid)
    d_winner(grid, result[1], turn)


if __name__ == '__main__':
    main()
