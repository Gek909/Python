import sympy

def get_result(expr, mode):
    if mode == 2:
        x = sympy.Symbol('x')
        try:
            result = sympy.simplify(expr)
            result = sympy.solve(expr, x)
            return result
        except:
            result = 'Incorrect input'
            return result
    elif mode == 1 or 3:
        try:
            result = sympy.simplify(expr)
            return result
        except:
            result = 'Incorrect input'
            return result




