
""""Example of shunting yard algorithm to evaluate
    math expressions including operators like +, -, *, /, ^, (, ),
    certain common functions and certain popular constants
    Supported functions:
    Exponential: exp, sqrt
    Logarithmic: ln, log
    Trigonometric: sin, cos, tan, asin, acos, atan
    Hyperbolic: sinh, cosh, tanh, asinh, acosh, atanh
    Supported constants:
    e, pi

    Notes: 1) This parser does not recognize implicit multiplication so please
              explicitly add '*' to indicate multiplication
           2) This parser ignores all whitespace, even between characters of a
              function name. This means 't a n ( 5 )' is as valid as 'tan(5)'
           3) However, as a result of note (2), functions with similar names will
              produce errors with whitespace. sin h(pi) produces an error as the parser
              recognizes sin, similarly with e xp(2) since e is a constant

              Basically, whitespace is fine but when spelling words it's best to avoid it"""

from Math_Functions import precedence as op_precedence
from Math_Functions import functions, constants, operators
from Helper_Functions import goodfix_helper, matching_bracket, evaluate, check_element


# Splits expression into its individual parts, operators and operands
def make_infix(expr, start=0, end=-1):
    result = []
    # slight adjustment to allow us to make expressions for specific parts
    if end == -1:
        end = len(expr)
    cur = []
    func = []
    skip_until = 0
    for i in range(start, end):
        # skip past stuff inside a function or parentheses pair
        if i < skip_until:
            continue
        char = expr[i]
        # ignore whitespace
        if char == " ":
            continue
        # handles the case of a matching function being found
        if "".join(func) in functions and char == '(':
            last = matching_bracket(expr, i)
            skip_until = last
            result.append(["".join(func), make_infix(expr, i+1, last-1)])
            func = []
        # makes everything inside a bracket basically a function to be handled
        # adjust bounds to exclude opening and closing brackets
        elif char == '(':
            last = matching_bracket(expr, i)
            skip_until = last
            result.append(make_infix(expr, i+1, last-1))
        elif char in op_precedence:
            if cur:
                result.append("".join(cur))
            cur = []
            result.append(char)
        # if its a letter it must be part of a function name or a constant
        elif char.isalpha():
            func.append(char)
        else:
            cur.append(char)

        # handles cases where what's stored in func is actually a constant
        # if it matches a constant, and it's either the last character (so it has to be a constant)
        # or the next character is not a letter (since no constants match functions then it must be a constant)
        if ("".join(func) in constants) and ((i == end-1) or (not expr[i+1].isalpha())):
            result.append("".join(func))
            func = []

        # to detect invalid function input, we look at 2 possibilities
        # 1) the longest function name is asinh with 5 characters so anything longer is incorrect
        # 2) we are currently building a function and the next
        #    character is not '(' or another letter so it's an invalid form
        if (len(func) > 5) or (func and not char.isalpha()):
            print("Expression contains an invalid function ->", "".join(func))
            return
    if cur:
        result.append("".join(cur))
    return result


# Further polishes the infix from make_infix to fix bugs with subtraction
def good_infix(expr):
    cur = []
    result = []
    subtracting = False
    skip_until = 0
    for i in range(len(expr)):
        if i < skip_until:
            continue
        op = expr[i]
        if type(op) is str and op in operators:
            if op == '-':
                subtracting = True
            if cur:
                cur.append(op)
            else:
                result = [result]+[op]
        else:
            if type(op) is list:
                op = good_infix(op)
            if subtracting:
                # finds the next "block" of the expression
                # the block is essentially everything connected by an operator with greater precedence than '-'
                next_op = goodfix_helper(expr, i)
                cur += next_op[0]
                skip_until = next_op[1]
                result += cur
                cur = []
                subtracting = False
            else:
                cur.append(op)

    result += cur
    return result


def make_postfix(expr):
    stack = []
    result = []
    for symbol in expr:
        # checks whether the symbol can be immediately added to stack
        if check_element(symbol, result):
            continue
        # if it's something we don't recognize then it's invalid
        elif symbol not in op_precedence:
            print(f"Invalid expression - unknown symbol -> {symbol}")
            return
        # if we have operators in our stack
        elif stack:
            # special case when the symbol is )
            if symbol == ')':
                # add everything on the stack onto the
                # result until matching ( is found
                while stack[-1] != '(':
                    result.append(stack.pop())
                    # if we get through the whole stack and none were (
                    # then we have an invalid expression
                    if not stack:
                        print(f"{expr}: invalid expression - unmatched ')'")
                        return
                # we found matching ( and must now remove it
                stack.pop()
            # compare precedence of symbol and top of stack
            # if current symbol is lower priority, we pop top of stack to result
            # and push symbol onto stack, else just push symbol onto stack
            elif op_precedence[symbol] > op_precedence[stack[-1]] and stack[-1] != '(':
                result.append(stack.pop())
                stack.append(symbol)
            else:
                stack.append(symbol)
        else:
            # push onto stack if it's empty
            stack.append(symbol)
    while stack:
        # at the end just pop all remaining symbols onto result
        # if we encounter ( then it didn't have a match so
        # expression is invalid
        if stack[-1] == '(':
            print(f"{expr}: invalid expression - leftover '(")
            return
        result.append(stack.pop())

    return result


def func_eval(parameter, func):
    # evaluates all function types (sin, log, etc)
    if func not in functions:
        print(f"{func} is not in the list of available functions")
        return
    input_postfix = make_postfix(parameter)
    value = evaluator(input_postfix)
    return functions[func](value)


def bracket_eval(elements):
    my_postfix = make_postfix(elements)
    value = evaluator(my_postfix)
    return value


# Function to evaluate postfix expressions
def evaluator(expr):
    stack = []
    for symbol in expr:
        if type(symbol) is list:
            # if len is 2 then its a function
            if len(symbol) == 2:
                value = func_eval(symbol[1], symbol[0])
            else:
                value = bracket_eval(symbol)
            stack.append(value)
        # if it's a number
        elif type(symbol) is float:
            stack.append(symbol)
        # if it's a constant
        elif symbol in constants:
            stack.append(constants[symbol])
        # if it's an operator
        else:
            # else it's an operator
            # if it's an operator and there's less than 2 numbers
            # then it's an invalid expression
            if len(stack) < 2:
                print(f"Inavlid postfix expression: {expr}")
                return
            # else, pop the last 2 elements and evaluate
            num2 = stack.pop()
            num1 = stack.pop()
            result = evaluate(num1, num2, symbol)
            stack.append(result)
    # if we have more than 1 number on the stack it was an
    # invalid expression
    if len(stack) != 1:
        print(f"{expr}: invalid postfix expression")
        return
    return stack.pop()


# example use case
def example(expr):
    print(f"After preprocessing, {expr} becomes:")
    infix = make_infix(expr)
    print(infix)
    goodfix = good_infix(infix)
    print(goodfix, 'better')
    postfix = make_postfix(goodfix)
    print("Then in postfix: ", postfix)
    print("which evaluates to: %.3f" % evaluator(postfix))


expr = "2+cos(pi/4)*tan( pi / 4 )+sin(3+pi-2-1-0- pi ) -10-2*100-1+ ln( e ) - log( 1  0 . 0 ^ 1 0 . 0)"
example(expr)
