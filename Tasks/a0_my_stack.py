"""
My little Stack
"""
from typing import Any

stack_list = []   # стек


def push(elem: Any) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global stack_list
    stack_list.append(elem)
    print(elem)
    return None

def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    global stack_list
    if stack_list:
        return stack_list.pop()
    else:
        return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    global stack_list
    print(ind)

    return stack_list[-1 - ind] if len(stack_list) > ind else None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global stack_list
    stack_list = []
    return None
