#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games import checking_for_even
from brain_games.games.base_loop import cycle_of_game


def main():
    cycle_of_game(checking_for_even)


if __name__ == '__main__':
    main()
