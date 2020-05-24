def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    counter = 0  # Счётчик, считающий сумму количества открытых и закрытых скобок.
    for i in brackets_row:
        if i == '(':
            counter +=1
        elif i == ')':
            counter -= 1
            if counter < 0:
                return False
    return True if counter == 0 else False

