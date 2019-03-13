#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Test iteration of the half of the string in the palindrome function.
"""
from unittest import TestCase

from palindrome.half import half


# noinspection PyTypeChecker
class TestHalf(TestCase):

    def test_half_is_one_character(self):
        p = "a"
        result = half(phrase=p)

        assert True is result

    def test_half_phrase_even_success(self):
        p = "noon"
        result = half(phrase=p)

        assert True is result

    def test_half_phrase_odd_success(self):
        p = "dad"
        result = half(phrase=p)

        assert True is result

    def test_half_when_phrase_is_empty(self):
        p = ""
        result = half(phrase=p)

        assert False is result

    def test_half_when_phrase_is_not_palindrome(self):
        p = "home"
        result = half(phrase=p)

        assert False is result

    def test_half_when_phrase_is_number(self):
        p = 101
        result = half(phrase=p)

        assert False is result

    def test_half_when_phrase_is_other_type(self):
        p = ["a", "b", "a"]
        result = half(phrase=p)

        assert False is result
