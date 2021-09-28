#!/usr/bin/env python
# -*- coding:utf-8 -*-

from brain_games.games.cli import welcome_user
from brain_games.games.checking_for_even import check_even

def main():
    name = welcome_user()
    check_even(name)


if __name__ == '__main__':
    main()
