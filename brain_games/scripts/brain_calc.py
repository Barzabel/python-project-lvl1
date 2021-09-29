#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.calc_game import calc
from brain_games.games.base_loop import loop


def main():
    loop(3, calc)


if __name__ == '__main__':
    main()
