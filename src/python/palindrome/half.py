#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Iterate the half of the string to check if it's the same of the second half of the string.
"""


def half(phrase: str) -> bool:
    """
    Iterate the half of string and figured out if it's palindrome or not.

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

    phrase_half = int(phrase_size / 2)

    start_time = default_timer()

    for index in range(0, phrase_half):
        if phrase[index] != phrase[-1 - index]:
            end_time = default_timer()
            final_time = start_time - end_time
            print('#%i Half is False: %f' % (phrase_size, final_time))
            return False

    end_time = default_timer()
    final_time = end_time - start_time
    print('#%i Half is True: %f' % (phrase_size, final_time))

    return True
