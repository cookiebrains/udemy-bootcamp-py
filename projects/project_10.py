# calculator
from input_files import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def output(n1):
    operation = input("Pick an operation:")
    n2 = float(input("What's the next number?:"))
    operation_function = operations[operation]
    answer = operation_function(n1, n2)
    return answer, operation, n2


def run():
    print(logo)
    n1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    keep_going = True
    while keep_going:
        answer, operation, n2 = output(n1)
        print(f'{n1} {operation} {n2} = {answer}')
        choose_to_cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.:")
        if choose_to_cont == 'y':
            n1 = answer
        if choose_to_cont == 'n':
            run()

