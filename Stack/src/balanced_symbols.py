from .stack import Stack


def balanced_parenthesis_checker(p_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(p_string) and balanced:
        value = p_string[index]
        if value == "(":
            s.push(value)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def balanced_symbols_checker(s_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(s_string) and balanced:
        value = s_string[index]

        if value in "([{":
            s.push(value)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, value):
                    balanced = False

        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False
