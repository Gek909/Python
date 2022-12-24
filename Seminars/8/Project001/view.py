import controller

def choose_mode():
    return int(input('1 = arithmetic operations; 2 = solution of the equations; 3 = symplifying polynomials; 4 = calc history   \nChoose mode: '))

def get_expr(mode):
    if mode == 2:
        return (input('Input the expression without "=": '))
    else:
        return (input('Input the expression: '))

def show_result(expr, result, mode):
    if mode == 1:
        print(f'{expr} = {result}')
    elif mode == 2:
        print(f'Equation root(s):\n{result}')
    elif mode == 3:
        print(f'Symplified polynomial:\n{result}')

def show_history(history):
    for i in range(len(history)):
        print(history[i])

def error_mode():
    print('Choose correct work mode (1 to 3)')