from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if elem < arr[0]:
        return None
    elif elem > arr[-1]:
        return None
    left_board = 0
    right_board = len(arr)
    while True:
        if elem == arr[int((left_board + right_board) / 2)]:

    return None
