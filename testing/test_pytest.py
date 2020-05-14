#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

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

    @pytest.mark.skipif(sys.version_info < (3,8), reason= '版本小于3.8不跑')
    @pytest.mark.parametrize('a', [1,2,3,4,6,8])
    @pytest.mark.parametrize('b',[48,24,16,12])
    def test_multiplication(self,a,b):
        result = self.calc.multiplication(a, b)
        assert result == 48

    def test_subtraction(self):
        result = self.calc.subtraction(2, 4)
        assert result == -2
