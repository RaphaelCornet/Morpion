from typing import Optional


def __filled(grid: list[list[int]], placement: tuple[int, int]) -> bool:
    return grid[placement[0]][placement[1]] != 1


def add(grid: list[list[int]], placement: tuple[int, int], player: int):
    grid[placement[0]][placement[1]] = player


def copy(grid: list[list[int]]) -> list[list[int]]:
    return [line for line in grid]


def create() -> list[list[int]]:
    return [[1 for _ in range(3)] for _ in range(3)]


def convert(move: int) -> tuple[int, int]:
    return (move - 1) // 3, (move - 1) % 3


def finish(grille) -> tuple[bool, Optional[int]]:
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] and grille[i][0] != 1:
            return True, grille[i][0]
    for j in range(3):
        if grille[0][j] == grille[1][j] == grille[2][j] and grille[0][j] != 1:
            return True, grille[0][j]
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != 1:
        return True, grille[0][0]
    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != 1:
        return True, grille[0][2]
    if all(grille[i][j] != 1 for i in range(3) for j in range(3)):
        return True, 1
    return False, None


def possibles(grid: list[list[int]]) -> list[tuple[int, int]]:
    return [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 1]


def remove(grid: list[list[int]], placement: tuple[int, int]):
    grid[placement[0]][placement[1]] = 1


def valid(grid: list[list[int]], move: str) -> bool:
    try:
        return 0 < int(move) < 10 and not __filled(grid, convert(int(move)))
    except ValueError:
        return False
