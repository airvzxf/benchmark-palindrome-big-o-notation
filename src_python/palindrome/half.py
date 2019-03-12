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
    if type(phrase) != str:
        return False

    phrase_size = len(phrase)

    if phrase_size == 0:
        return False

    phrase_half = int(phrase_size / 2)

    for index in range(0, phrase_half):
        if phrase[index] != phrase[-1 - index]:
            return False

    return True
