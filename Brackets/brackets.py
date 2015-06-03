def isOpening(brace):
        return brace == '{' or brace == '[' or brace == '('


def isClosing(brace):
        return brace == ')' or brace == ']' or brace == '}'


def isEmpty(stack):
    return len(stack) == 0


def isDigit(sym):
    return sym in '0123456789'


def sumUntilOpening(stack):
        suma = 0
        base = 1
        temp = stack.pop()
        while isOpening(temp[0]) is False:
            if temp[0] == '+':
                suma += int(temp)
                base = 1
            else:
                suma += base * int(temp)
                base *= 10
            if isEmpty(stack):
                break
            else:
                temp = stack.pop()
        if not isEmpty(stack):
            suma = 2 * suma
        stack.append("+" + str(suma))


def evaluate(expr):
    stack = []
    for i in range(len(expr)):
        if isOpening(expr[i]) or isDigit(expr[i]):
            stack.append(expr[i])
        elif isClosing(expr[i]):
            sumUntilOpening(stack)
    return int(stack.pop())


def bracket_validation(string):
    stack = []
    for x in string:
        if x == "{":
            stack.append(x)
        elif x == "(":
            stack.append(x)
        elif x == "[":
            stack.append(x)
    if "(" in string and "{" in string:
        if string.index("(") < string.index('{') and string.index("}") < string.index(")"):
            return "NO"
    if "(" in string and "[" in string:
        if string.index("(") < string.index('[') and string.index("]") < string.index(")"):
            return "NO"
    if "[" in string and "{" in string:
        if string.index("[") < string.index("{"):
            return "NO"
    if '{' in string:
        if stack.count('{') > 1 or stack.index("{") != 0:
            return "NO"
    if "(" in stack and "{" in stack:
        if stack.index("{") == stack.index("(") - 1:
            return "NO"
    while len(stack) != 0:
        for x in string:
            if x in ["]", "}", ")"]:
                if x == ")" and stack[len(stack) - 1] == "(":
                    stack.pop()
                elif x == "]" and stack[len(stack) - 1] == "[":
                    stack.pop()
                elif x == "}" and stack[len(stack) - 1] == "{":
                    stack.pop()
                else:
                    return "NO"
    return evaluate(string)


def main():
    print(bracket_validation("[123(145)38(37)812]"))
    print(bracket_validation("{125[2][(1)][3]125}"))
    print(bracket_validation("[125()125()125()125]"))
    print(bracket_validation("{125()125}"))
    print(bracket_validation("{125[12]{125}[12]125}"))
    print(bracket_validation("{125[12(123]125}"))

if __name__ == '__main__':
    main()
