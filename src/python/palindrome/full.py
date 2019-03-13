#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Iterate the full the string instead the half of the string is correct.
"""


def full(phrase: str) -> bool:
    """
    Iterate the whole string and figured out if it's palindrome or not.

    :rtype input: str
    :param phrase: The string with the tentative palindrome phrase.

    :rtype: bool
    :return: True if the string is palindrome otherwise returns false
    """
    from timeit import default_timer

    if type(phrase) != str:
        return False

    phrase_size = len(phrase)

    if phrase_size == 0:
        return False

    start_time = default_timer()

    for index in range(0, phrase_size):
        if phrase[index] != phrase[-1 - index]:
            end_time = default_timer()
            final_time = start_time - end_time
            print('#%i Full is False: %f' % (phrase_size, final_time))
            return False

    end_time = default_timer()
    final_time = end_time - start_time
    print('#%i Full is True: %f' % (phrase_size, final_time))

    return True
