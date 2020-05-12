#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from python.calc import Calc


class TestCalc:
    # @pytest.mark.parametrize()
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,expect",
                             [
                                 (0, 0, 0),
                                 (1, 2, 3),
                                 (-1, 1, 0)])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.parametrize("a,b,expect",
                             [
                                 (0, 1, 0),
                                 (2, 1, 2),
                                 (-1, 1, -1),
                                 (2, 0, 'ZeroDivisionError'),
                                 (2,3,2/3)
                             ])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert expect == result

    def test_multiplication(self):
        result = self.calc.multiplication(2, 3)
        assert result == 6

    def test_subtraction(self):
        result = self.calc.subtraction(2, 4)
        assert result == -2
