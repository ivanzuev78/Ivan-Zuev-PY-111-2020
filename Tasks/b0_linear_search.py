"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    minimum = arr[0]
    index = 0
    for ind, val in enumerate(arr):
        if minimum > val:
            minimum = val
            index = ind
    return index
