from typing import Optional


def __filled(grid: list[list[int]], placement: tuple[int, int]) -> bool:
    """
    Check if the placement is filled or not

    :param grid: The grid of the current game
    :param placement: The placement which is checked
    """
    return grid[placement[0]][placement[1]] != 1


def add(grid: list[list[int]], placement: tuple[int, int], player: int):
    """
    Add a value to the grid

    :param grid: The grid of the current game
    :param placement: The placement which is filled
    :param player: The player who's playing
    """
    grid[placement[0]][placement[1]] = player


def create() -> list[list[int]]:
    """
    Create the grid
    """
    return [[1 for _ in range(3)] for _ in range(3)]


def convert(move: int) -> tuple[int, int]:
    """
    Convert the move (an int between 1 and 9) into the placement of the corresponding cell

    :param move: The move converted
    """
    return (move - 1) // 3, (move - 1) % 3


def finish(grid) -> tuple[bool, Optional[int]]:
    """
    Return if the game is finished or not, if it is, return also the player

    :param grid: The grid of the current game
    """
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != 1:
            return True, grid[i][0]
    for j in range(3):
        if grid[0][j] == grid[1][j] == grid[2][j] and grid[0][j] != 1:
            return True, grid[0][j]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != 1:
        return True, grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != 1:
        return True, grid[0][2]
    if all(grid[i][j] != 1 for i in range(3) for j in range(3)):
        return True, 1
    return False, None


def possibles(grid: list[list[int]]) -> list[tuple[int, int]]:
    """
    Return the list of all possible moves of the grid

    :param grid: The grid of the current game
    """
    return [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 1]


def remove(grid: list[list[int]], placement: tuple[int, int]):
    """
    Remove a value from the grid

    :param grid: The grid of the current game
    :param placement: The placement which is emptied
    """
    grid[placement[0]][placement[1]] = 1


def valid(grid: list[list[int]], move: str) -> bool:
    """
    Return whether the move is valid

    :param grid: The grid of the current game
    :param move: The move that is tested
    """
    try:
        return 0 < int(move) < 10 and not __filled(grid, convert(int(move)))
    except ValueError:
        return False
