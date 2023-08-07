#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.calc_game import game_calc, DESCRIPTION
from brain_games.games.base_loop import cycle_of_game


def main():
    cycle_of_game(game_calc, DESCRIPTION)


if __name__ == '__main__':
    main()
