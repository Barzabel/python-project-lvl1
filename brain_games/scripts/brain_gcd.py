#!/usr/bin/env python
# -*- coding:utf-8 -*-
from brain_games.games.game_nod import game_nod
from brain_games.games.base_loop import loop


def main():
    loop(3, game_nod)


if __name__ == '__main__':
    main()
