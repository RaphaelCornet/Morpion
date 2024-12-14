from random import choice
from typing import Optional

import grid_manager


def __ask(grid: list[list[int]]) -> int:
    """
    Ask the user to enter a number corresponding to the grid cell where he wants to play.

    :param grid: The grid of the current game
    """
    move: str = input("Où souhaitez-vous mettre une croix ? ")
    while not grid_manager.valid(grid, move):
        print("Coup invalide =<")
        move = input("Où souhaitez-vous mettre une croix ? ")
    print()
    return int(move)


def __best(grid) -> tuple[int, int]:
    """
    Return the best possible placement in the current grid using the minimax algorithms

    :param grid: The grid of the current game
    """
    best_placement: Optional[tuple[int, int]] = None
    best_score: float = float("-inf")
    for placement in grid_manager.possibles(grid):
        grid_manager.add(grid, placement, 2)
        score: float = __eval(grid, 0)
        grid_manager.remove(grid, placement)
        if score > best_score:
            best_score = score
            best_placement = placement
    return best_placement


def __eval(grid: list[list[int]], player: int) -> float:
    """
    Return the evaluation of the current grid for the player

    :param grid: The grid that is tested
    :param player: The player for which the evaluation is desired
    """
    result: tuple[bool, Optional[int]] = grid_manager.finish(grid)
    if result[0]:
        if result[1] == 2:
            return 1
        elif result[1] == 0:
            return -1
        else:
            return 0

    if player == 0:
        best_score = float("-inf")
    else:
        best_score = float("+inf")
    for placement in grid_manager.possibles(grid):
        grid_manager.add(grid, placement, player)
        if player == 0:
            score: float = __eval(grid, 2)
        else:
            score: float = __eval(grid, 0)
        grid_manager.remove(grid, placement)
        if player == 0:
            best_score = min(best_score, score)
        else:
            best_score = max(best_score, score)
    return best_score


def computer_turn(grid: list[list[int]]):
    """
    Do the computer turn

    :param grid: The grid of the current game
    """
    best_move = __best(grid)
    grid_manager.add(grid, best_move, 2)


def human_turn(grid: list[list[int]]):
    """
    Do the human turn

    :param grid: The grid of the current game
    """
    move: int = __ask(grid)
    placement: tuple[int, int] = grid_manager.convert(move)
    grid_manager.add(grid, placement, 0)


def random() -> int:
    return choice([0, 2])
