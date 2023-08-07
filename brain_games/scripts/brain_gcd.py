#!/usr/bin/env python
# -*- coding:utf-8 -*-
from brain_games.games.game_nod import game_nod, DESCRIPTION
from brain_games.games.base_loop import cycle_of_game


def main():
    cycle_of_game(game_nod, DESCRIPTION)


if __name__ == '__main__':
    main()
