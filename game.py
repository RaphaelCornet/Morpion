from typing import Optional, Callable

import database_manager
import display_manager
import grid_manager
import player_manager


class Game:
    def __init__(self, identifier: int):
        self.__identifier = identifier
        self.__name = input("Quel est votre pseudonyme ?\n")
        self.__grid: list[list[int]] = grid_manager.create()
        self.__turn_order: Callable = self.__corresponding_method(player_manager.random_turn())
        self.__current_turn: int = 0
        self.__result: tuple[bool, Optional[int]] = False, None

    def __corresponding_method(self, func: int) -> Callable:
        if func == 0:
            return self.__player_first
        elif func == 2:
            return self.__computer_first
        else:
            raise ValueError(f"Function n°{func} don't exist.")

    def __computer_first(self):
        player_manager.computer_turn(self.__grid)
        self.__result = grid_manager.finish(self.__grid)
        if self.__result[0]:
            return
        display_manager.grid(self.__grid)
        player_manager.human_turn(self.__grid)

    def __player_first(self):
        display_manager.grid(self.__grid)
        player_manager.human_turn(self.__grid)
        self.__result = grid_manager.finish(self.__grid)
        if self.__result[0]:
            return
        player_manager.computer_turn(self.__grid)

    def __turn(self):
        self.__current_turn += 1
        print(f"--- Tour n°{self.__current_turn} ---\n")
        self.__turn_order()
        self.__result = grid_manager.finish(self.__grid)

    def __winner(self) -> str:
        match self.__result[1]:
            case 0:
                return self.__name
            case 1:
                "Tie"
            case 2:
                "AI"
            case _:
                raise ValueError(f"Player n°{self.__result[1]} don't exist.")

    def start(self):
        while not self.__result[0]:
            self.__turn()

        display_manager.winner(self.__grid, self.__result[1], self.__current_turn)
        database_manager.register(self.__identifier, self.__name, self.__winner(), self.__grid, self.__current_turn)
