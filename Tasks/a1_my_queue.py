"""
My little Queue
"""
from typing import Any

deque_list = []  # начало слева, конец ( добавление ) справа


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global deque_list
    deque_list.append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    global deque_list
    if deque_list:
        return deque_list.pop(0)
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global deque_list
    return deque_list[ind] if len(deque_list) > ind else None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global deque_list
    deque_list = []
    return None
