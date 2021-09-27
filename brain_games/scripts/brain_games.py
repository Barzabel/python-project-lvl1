#!/usr/bin/env python  
# -*- coding:utf-8 -*-
import prompt

def main():
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print("Hello, {}!".format(name))

if __name__ == '__main__':
    main()