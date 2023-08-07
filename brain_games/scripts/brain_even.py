#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.checking_for_even import game_check_even, DESCRIPTION
from brain_games.games.base_loop import cycle_of_game


def main():
    cycle_of_game(game_check_even, DESCRIPTION)


if __name__ == '__main__':
    main()
