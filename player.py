from random import choice
from typing import Callable, Optional

from grid import add, convert, finish, possibles, remove, valid


def __ask(grid: list[list[int]]) -> int:
    move: str = input("Où souhaitez-vous mettre une croix ? ")
    while not valid(grid, move):
        print("Coup invalide =<")
        move = input("Où souhaitez-vous mettre une croix ? ")
    print()
    return int(move)


def __best(grid) -> tuple[int, int]:
    best_placement: Optional[tuple[int, int]] = None
    best_score: float = float("-inf")
    for placement in possibles(grid):
        add(grid, placement, 2)
        score: float = __eval(grid, 0)
        remove(grid, placement)
        print(score)
        if score > best_score:
            best_score = score
            best_placement = placement
    return best_placement


def __corresponding(player: int) -> Callable[[float, float], float]:
    return max if player == 2 else min


def __default_score(player: int) -> float:
    return float("-inf") if player == 2 else float("+inf")


def __eval(grid: list[list[int]], player: int) -> float:
    result: tuple[bool, Optional[int]] = finish(grid)
    if result[0]:
        if result[1] == 2:
            return 1
        elif result[1] == 0:
            print("a")
            return -1
        else:
            return 0
    best_score: float = __default_score(player)
    for placement in possibles(grid):
        add(grid, placement, player)
        score: float = __eval(grid, __other(player))
        remove(grid, placement)
        best_score = __corresponding(player)(best_score, score)
    return best_score


def __other(player: int) -> int:
    return 0 if player == 2 else 2


def computer_turn(grid: list[list[int]]):
    best_move = __best(grid)
    add(grid, best_move, 2)


def human_turn(grid: list[list[int]]):
    move: int = __ask(grid)
    placement: tuple[int, int] = convert(move)
    add(grid, placement, 0)


def random() -> int:
    return choice([0, 2])
