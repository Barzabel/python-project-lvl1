#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.game_prime import game_prime, DESCRIPTION
from brain_games.games.base_loop import cycle_of_game


def main():
    cycle_of_game(game_prime, DESCRIPTION)


if __name__ == '__main__':
    main()
