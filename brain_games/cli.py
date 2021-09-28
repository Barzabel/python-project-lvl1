# coding=utf-8

import prompt
""" greeting users, ask name"""


def welcome_user():
    """ greeting users, ask name """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
