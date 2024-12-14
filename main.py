from typing import Optional

import display_manager
import grid_manager
import player_manager


def main():
    """
    The main function of this project
    """
    grid: list[list[int]] = grid_manager.create()
    starter: int = player_manager.random()
    turn: int = 0
    result: tuple[bool, Optional[int]] = False, None
    while not result[0]:
        turn += 1
        print(f"--- Tour n°{turn} ---\n")
        if starter == 0:
            display_manager.grid(grid)
            player_manager.human_turn(grid)
            result = grid_manager.finish(grid)
            if result[0]:
                break
            player_manager.computer_turn(grid)
        elif starter == 2:
            player_manager.computer_turn(grid)
            result = grid_manager.finish(grid)
            if result[0]:
                break
            display_manager.grid(grid)
            player_manager.human_turn(grid)
        result = grid_manager.finish(grid)
    display_manager.winner(grid, result[1], turn)


if __name__ == '__main__':
    main()
