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
        actual = int((left_board + right_board) / 2)
        if elem == arr[actual]:
            # return actual
            sdvig = 1
            while True:
                if actual - sdvig < 0:
                    return 0
                elif elem == arr[actual - sdvig]:
                    sdvig += 1
                else:
                    return actual - sdvig + 1
        elif right_board - left_board == 1:
            return None
        elif elem > arr[actual]:
            left_board = actual
        elif elem < arr[actual]:
            right_board = actual


    return None
