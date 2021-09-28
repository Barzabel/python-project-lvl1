#!/usr/bin/env python
# -*- coding:utf-8 -*-
from brain_games import checking_for_even
from brain_games import cli


def main():
    name = cli.welcome_user()
    checking_for_even.check_even(name)


if __name__ == '__main__':
    main()
