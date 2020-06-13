from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container
    else:
        mid = len(container) // 2
        first_mid = sort(container[:mid])
        second_mid = sort(container[mid:])
        sorted_list = []
        while first_mid and second_mid:
            if first_mid[0] > second_mid[0]:
                sorted_list.append(second_mid.pop(0))
            else:
                sorted_list.append(first_mid.pop(0))
        if first_mid:
            sorted_list += first_mid
        elif second_mid:
            sorted_list += second_mid
        return sorted_list
