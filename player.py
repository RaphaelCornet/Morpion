from random import choice
from typing import Callable, Optional

from constants import GRID_SIDE
from grid import valid, add, convert, possibles, finish, remove


def __ask(grid: list[list[int]]) -> int:
    move: str = input("Où souhaitez-vous mettre une croix ? ")
    while not valid(grid, move):
        print("Coup invalide =<")
        move = input("Où souhaitez-vous mettre une croix ? ")
    print()
    return int(move)


def __corresponding(player: int) -> Callable[[list[int]], int]:
    return max if player == 0 else min


def __other(player: int) -> int:
    return 0 if player == 2 else 2


def __default_score(player: int) -> float:
    return float("-inf") if player == 0 else float("+inf")


def __eval(grid, player) -> float:
    result: tuple[bool, Optional[int]] = finish(grid)
    if result[0]:
        return result[1]
    best_score: float = __default_score(player)
    for placement in possibles(grid):
        add(grid, placement, player)
        score: float = __eval(grid, __other(player))
        remove(grid, placement)
        best_score = __corresponding(player)(best_score, score)
    return best_score

def __best(grid) -> tuple[int, int]:
    best_placement: Optional[tuple[int, int]] = None
    best_score: float = float("-inf")
    for placement in possibles(grid):
        add(grid, placement, 2)
        score: float = __eval(grid, 0)
        add(grid, placement, 1)
        if score > best_score:
            best_score = score
            best_placement = placement
    return best_placement


def computer_turn(grid: list[list[int]], turn: int):
    if turn == 0:
        add(grid, (GRID_SIDE // 2, GRID_SIDE // 2), 2)
        return
    placement: tuple[int, int] = __best(grid)
    add(grid, placement, 2)


def human_turn(grid: list[list[int]]):
    move: int = __ask(grid)
    placement: tuple[int, int] = convert(move)
    add(grid, placement, 0)


def random() -> int:
    return choice([0, 2])
