#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games import calc_game
from brain_games.base_loop import cycle_of_game


def main():
    cycle_of_game(calc_game)


if __name__ == '__main__':
    main()
