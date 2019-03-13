#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Test for full iterator in the palindrome function.
"""
from unittest import TestCase

from palindrome.full import full


# noinspection PyTypeChecker
class TestFull(TestCase):

    def test_full_is_one_character(self):
        p = "a"
        result = full(phrase=p)

        assert True is result

    def test_full_phrase_even_success(self):
        p = "noon"
        result = full(phrase=p)

        assert True is result

    def test_full_phrase_odd_success(self):
        p = "dad"
        result = full(phrase=p)

        assert True is result

    def test_full_when_phrase_is_empty(self):
        p = ""
        result = full(phrase=p)

        assert False is result

    def test_full_when_phrase_is_not_palindrome(self):
        p = "home"
        result = full(phrase=p)

        assert False is result

    def test_full_when_phrase_is_number(self):
        p = 101
        result = full(phrase=p)

        assert False is result

    def test_full_when_phrase_is_other_type(self):
        p = ["a", "b", "a"]
        result = full(phrase=p)

        assert False is result
