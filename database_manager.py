from sqlite3 import connect, Cursor, OperationalError
from typing import Optional

import display_manager

DB_NAME: str = "morpion_database.db"

cursor: Optional[Cursor] = None


def __load():
    global cursor
    cursor = connect(DB_NAME).cursor()


def __register(identifier, name, winner, grid, turn):
    cursor.execute(
        """
        INSERT INTO morpion (id, name, winner, grid, turn)
        VALUES (?, ?, ?, ?, ?)
        """,
        (identifier, name, winner, display_manager.grid_appearance(grid), turn)
    )


def create_table():
    global cursor
    if cursor is None:
        __load()
    assert type(cursor) == Cursor

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS 'morpion' (
            id  INT PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            winner VARCHAR(100),
            grid VARCHAR(75) NOT NULL,
            turn INT NOT NULL
        )
        """
    )


def register(identifier: int, name: str, winner: str, grid: list[list[int]], turn: int):
    global cursor
    if cursor is None:
        __load()
    assert type(cursor) == Cursor

    try:
        __register(identifier, name, winner, grid, turn)
    except OperationalError:
        create_table()
        __register(identifier, name, winner, grid, turn)
