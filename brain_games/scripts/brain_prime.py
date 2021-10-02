#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.game_prime import game_prime
from brain_games.games.base_loop import loop


def main():
    loop(3, game_prime)


if __name__ == '__main__':
    main()
