#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "sondos with help from Gabby and Shanqual"
# https://www.programmersought.com/article/74581508841/


import random
import sys


def create_mimic_dict(filename):

    mimic_dict = dict()
    with open(filename) as f:
        text = f.read()
        words = text.split()
        prev_word = ''
        for word in words:
            if prev_word in mimic_dict:
                mimic_dict[prev_word].append(word)
            else:
                mimic_dict[prev_word] = [word]
            prev_word = word
    return mimic_dict


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    start_word = ''
    for ___ in range(num_words + 1):
        next_word = mimic_dict.get(start_word)
        print(start_word, end=' ')
        if next_word is None:
            next_word = mimic_dict['']
        start_word = random.choice(next_word)


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
