from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    import random

    def local_sort(start_ind=0, end_ind=len(container) - 1):  # Функция, которая сортирует контейнер между двумя индексами
        if end_ind - start_ind <= 2:  # Если приходят 2 индекса рядом, то она считает этот кусок отсортированым
            return None
        start, end = start_ind, end_ind  # Запоминаем старт и конец (потом понадобится)
        opora = container[random.randint(start_ind, end_ind)]  # Опорный элемент
        local_search = True  # Флаг для окончания сортировки
        while local_search:  # Запуск локальной сортировки
            while container[start_ind] < opora:  # Ищем элемент слева меньше опорного
                start_ind += 1
            while container[end_ind] > opora:  # Ищем элемент справа больше опорного
                end_ind -= 1
            if end_ind > start_ind:  # Меняем местами, если они друг друга не обошли
                container[start_ind], container[end_ind] = container[end_ind], container[start_ind]
            if start_ind - end_ind < 1:  # Если они друг друга обошли, прекращаем сортировку и сортируем правый и левый кусок
                local_search = False
                local_sort(start, end_ind)  # Сортируем левый кусок
                local_sort(start_ind, end)  # Сортируем правый кусок


    local_sort()  # Запускаем сортировку

    return container
