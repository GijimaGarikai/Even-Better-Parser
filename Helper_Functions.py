import re
from Math_Functions import operators, constants
from Math_Functions import precedence as op_precedence


def is_integer_or_decimal(word):
    pattern = r"^[+-]?\d+(\.\d+)?$"
    return bool(re.match(pattern, word))


# help us find what characters belong to a set of parentheses by finding the position of it's matching bracket
def matching_bracket(word, start):
    if word[start] != '(':
        print("function not followed by '(' therefore invalid")
        return
    total = 0
    for i in range(start, len(word)):
        if word[i] == '(':
            total += 1
        elif word[i] == ')':
            total -= 1
        if total == 0:
            return i + 1
    print("Invalid expression, unmatched '('")
    return


# checks whether element can be immediately added to stack
def check_element(element, stack):
    # if it's a list then it's a function, just add as is
    if type(element) is list:
        stack.append(element)
    # if it's a constant add as is
    elif element in constants:
        stack.append(element)
    # if it's a number just add to postfix result
    elif is_integer_or_decimal(element):
        stack.append(float(element))
    else:
        return False
    return True

# Evaluator helper
def evaluate(num1, num2, operator):
    if operator not in operators:
        print(f"{operator} not in list of operators")
        return
    return operators[operator](num1, num2)


