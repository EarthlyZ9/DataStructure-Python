from src.deque import Deque
from src.palindrome import palindrome_checker

print("========= Basic Queue =========")
d = Deque()
print(d.is_empty())
d.add_rear(4)
d.add_rear("dog")
d.add_front("cat")
d.add_front(True)
print(d.size())
print(d.is_empty())
d.add_rear(8.4)
print(d.remove_rear())
print(d.remove_front())

print("========= Palindrome Checker =========")
print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))
