from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

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
    actual = int((left_board + right_board) / 2)
    if elem == arr[actual]:  # Тут линейный поиск элемента, когда одинаковые идут подряд
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
        result = binary_search(elem, arr[actual:])
        if not result:  # Проверка, возвращается None или нет
            return result # Если возвращается None, прокидываем его дальше
        else:
            return actual + result
    elif elem < arr[actual]:
        result =  binary_search(elem, arr[0:actual])
        if not result:  # Проверка, возвращается None или нет
            return result  # Если возвращается None, прокидываем его дальше
        else:
            return result

    return None
