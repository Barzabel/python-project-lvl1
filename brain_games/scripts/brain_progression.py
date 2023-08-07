#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.progression_game import game_progression, DESCRIPTION
from brain_games.games.base_loop import cycle_of_game


def main():
    cycle_of_game(game_progression, DESCRIPTION)


if __name__ == '__main__':
    main()
