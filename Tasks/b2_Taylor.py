"""
Taylor series
"""
from typing import Union
from math import factorial
from itertools import count

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    result = 0
    for n in count():
        delta = (x ** n) / factorial(n)
        result += delta
        if delta < 0.0001:
            break

    return result


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    result = 0
    for n in count():
        delta = (-1) ** n * ( x ** (2 * n + 1) / factorial(2 * n + 1))
        result_prev = result
        result += delta
        if abs(result - result_prev) < 0.0001:
            break
    return result
