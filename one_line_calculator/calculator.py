import re

def turn_into_list(expression):
    expression = re.sub('[*]{2}', '^', expression)
    expression = re.sub('[x]|[X]', '*', expression)

    # Need a function to check if it is a correct expression
    # also to check if any numbers are missing e.g. 2/^4
    check_begin = expression[0]
    check_end = expression[-1]
    check_symbols = ['*', '/', '^']

    if check_begin in check_symbols or check_end in check_symbols:
        print("There's something wrong with this expression.. %s" % expression)
        calculator()

    expression_list, temp_list = [], []
    minus_index, plus_index = 0, 0
    # Also need to add function if starts with + or - or 2*+3 same as 2*3 and
    # 2*-3 is 2*(-3)

    for character in expression:
        try:
            int(character)
            temp_list.append(character)
            minus_index, plus_index = 0, 0
        except Exception as e:
            if character == '-':
                minus_index += 1
            elif character == '+':
                plus_index += 1

            if minus_index == 2 or plus_index == 2:
                expression_list.pop()
                expression_list.append('+')
            elif minus_index == 1 and plus_index == 1:
                expression_list.pop()
                expression_list.append('-')
            else:
                expression_list.append("".join(temp_list))
                expression_list.append(character)
                temp_list = []

    expression_list.append(expression[-1])

    return expression_list

def addition(number, number_2):
    return number + number_2

def subtraction(number, number_2):
    return number - number_2

def multiplication(number, number_2):
    return number * number_2

def division(number, number_2):
    return number / number_2

def power(number, number_2):
    return number ** number_2

def expression():
    expression = input(">> ")
    expression = re.sub('\s+', '', expression)
    return expression

def get_selection(number, symbol, number_2):
    symbols = {
        '+' : addition,
        '-' : subtraction,
        '/' : division,
        '*' : multiplication,
        '^' : power
    }
    answer = symbols.get(symbol, lambda: "nothing")
    return answer(number, number_2)

def calculate(expression):
    expression = turn_into_list(expression)

    def solve():
        number       = int(expression[index])
        symbol       = expression[index + 1]
        number_2     = int(expression[index + 2])
        new_solution = get_selection(number, symbol, number_2)

        # Deletes numbers that have been used
        [expression.pop(index) for _ in range(3)]
        # Replaces last number with new solution number
        expression.insert(index, new_solution)

    while len(expression) != 1:
        index = 0

        if '^' in expression:
            index = expression.index('^') - 1
            solve()

        elif '*' in expression or '/' in expression:
            if '*' in expression:
                multiply_index = expression.index('*')
            else:
                multiply_index = len(expression)

            if '/' in expression:
                division_index  = expression.index('/')
            else:
                division_index = len(expression)

            if multiply_index < division_index:
                index = multiply_index - 1
            else:
                index = division_index - 1

            solve()

        else:
            if '+' in expression:
                addition_index = expression.index('+')
            else:
                addition_index = len(expression)

            if '-' in expression:
                subtraction_index  = expression.index('-')
            else:
                subtraction_index = len(expression)

            if addition_index < subtraction_index:
                index = addition_index - 1
            else:
                index = subtraction_index - 1

            solve()


    return expression[0]

def calculator():
    start = expression()
    solution = calculate(start)
    print("This is the solution: %s" % solution)

# calculator()
