"""
Taylor series
"""
from typing import Union
from math import factorial

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    result = 0
    for n in range(100):
        result += (x ** n) / factorial(n)

    return result


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    result = 0
    for n in range(50):
        result += (-1) ** n * ( x ** (2 * n + 1) / factorial(2 * n + 1))
    return result
