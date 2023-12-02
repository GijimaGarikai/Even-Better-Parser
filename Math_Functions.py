"""File for all math functions and operators used in parser"""

import math
from Operator_functions import add, sub, div, mult

precedence = {'(': 1, ')': 1, '^': 1.5, '*': 2, '/': 2,
              '+': 3, '-': 3}
operators = {'^': math.pow, '*': mult, '/': div,
             '+': add, '-': sub}
functions = {'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'asin': math.asin, 'acos': math.acos,
             'atan': math.atan, 'ln': math.log, 'log': math.log10, 'sinh': math.sinh, 'cosh': math.cosh,
             'tanh': math.tanh, 'asinh': math.asinh, 'acosh': math.acosh, 'atanh': math.atanh,
             'exp': math.exp, 'sqrt': math.sqrt}
constants = {'e': math.e, 'pi': math.pi}
