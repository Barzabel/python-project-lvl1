#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.progression_game import progression_game
from brain_games.games.base_loop import loop


def main():
    loop(3, progression_game)


if __name__ == '__main__':
    main()
