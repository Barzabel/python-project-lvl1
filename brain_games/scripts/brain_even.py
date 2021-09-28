#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.checking_for_even import check_even
from brain_games.games.base_loop import loop


def main():
    loop(3, check_even)


if __name__ == '__main__':
    main()
