from .stack import Stack


def infix_to_postfix(infix_exp):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_exp.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:  # 연산자라면
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfix_eval(postfix_exp):
    operands_stack = Stack()
    postfix_list = postfix_exp.split()

    for token in postfix_list:
        if token in "0123456789":
            operands_stack.push(int(token))
        else:
            operand2 = operands_stack.pop()
            operand1 = operands_stack.pop()

            cal = do_math(token, operand1, operand2)
            operands_stack.push(cal)

    return operands_stack.pop()
