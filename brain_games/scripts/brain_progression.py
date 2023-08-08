#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games import progression_game
from brain_games.games.base_loop import cycle_of_game


def main():
    cycle_of_game(progression_game)


if __name__ == '__main__':
    main()
