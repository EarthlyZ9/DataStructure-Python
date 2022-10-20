"""
palindrome: 왼쪽으로 읽으나 오른쪽으로 읽으나 같은 단어

- front 와 rear 양쪽에서 꺼내서 같은지 비교함

"""

from deque import Deque


def palindrome_checker(p_str):
    char_deque = Deque()

    for ch in p_str:
        char_deque.add_rear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()

        if first != last:
            still_equal = False

    return still_equal
