#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Main script which start the benchmark.
"""


# noinspection PyCompatibility
def main() -> None:
    """
    Start the python benchmarks between iterate the full string and iterate the half of the string.

    :rtype: None
    """
    from timeit import timeit

    files = [
        './resources/01-small.txt',
        # './resources/02-medium.txt',
        # './resources/03-big.txt',
        # './resources/04-huge.txt',
    ]

    for file in files:
        with open(file) as phrase_file:
            phrase_full = phrase_file.read()

        with open(file) as phrase_file:
            phrase_half = phrase_file.read()

        print('File: %s\n' % file)

        print('Phrase for full. Memory address: %s' % hex(id(phrase_full)))
        print('Phrase for half. Memory address: %s\n' % hex(id(phrase_half)))

        print('Size: %i characters.\n' % int(len(phrase_full)))

        print('half: %f s' % timeit("half('" + phrase_half + "')", setup="from palindrome.half import half"))
        print('full: %f s' % timeit("full('" + phrase_full + "')", setup="from palindrome.full import full"))

        print('\n\n')

    return None


if __name__ == "__main__":
    main()
