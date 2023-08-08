#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games import game_progression
from brain_games.games.base_loop import cycle_of_game


def main():
    cycle_of_game(game_progression)


if __name__ == '__main__':
    main()
