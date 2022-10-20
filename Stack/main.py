from src.stack import Stack
from src.balanced_symbols import balanced_parenthesis_checker, balanced_symbols_checker
from src.to_binary_number import divide_by_2, base_converter
from src.postfix import infix_to_postfix, postfix_eval


print("========= Basic src Class =========")
s = Stack()

print(s.is_empty())
s.push(4)
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

print("========= Balanced Parenthesis =========")
print(balanced_parenthesis_checker("((()))"))
print(balanced_parenthesis_checker("(()"))
print("========= Balanced Symbols =========")
print(balanced_symbols_checker("{({([][])}())}"))
print(balanced_symbols_checker("[{()]"))

print("========= Binary Expression =========")
print(divide_by_2(42))
print(base_converter(25, 8))
print(base_converter(256, 16))
print(base_converter(26, 26))

print("========= Infix to Postfix =========")
print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

print("========= Postfix Evaluation =========")
print(postfix_eval("7 8 + 3 2 + /"))
