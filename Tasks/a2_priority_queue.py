"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

# from _collections import deque

COUNT_PRIORITY = 11
priority_queue = {p: [] for p in range(COUNT_PRIORITY)}

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global COUNT_PRIORITY, priority_queue
    if priority in range(COUNT_PRIORITY):
        priority_queue[priority].append(elem)
    elif priority > COUNT_PRIORITY:
        priority_queue[COUNT_PRIORITY].append(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global priority_queue, COUNT_PRIORITY
    for i in range(COUNT_PRIORITY):
        if priority_queue[i]:
            return priority_queue[i].pop(0)
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global COUNT_PRIORITY, priority_queue
    full_que = []
    for i in range(COUNT_PRIORITY):
        full_que += priority_queue[i]
    return full_que[ind]
    # Дописть

    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_queue
    priority_queue = {p: [] for p in range(COUNT_PRIORITY)}
    return None
