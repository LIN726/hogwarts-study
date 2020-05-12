#!/usr/bin/env python
# -*- coding: utf-8 -*-
# type hints 类型提示
class Calc:

    def add(self, a: int, b: int):
        return a + b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return 'ZeroDivisionError'


    def multiplication(self, a, b):
        return a * b

    def subtraction(self, a, b):
        return a - b
