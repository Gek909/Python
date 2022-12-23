import sympy

def get_result(expr, mode):
    if mode == 2:
        result = sympy.simplify(expr)
        x = sympy.Symbol('x')
        result = sympy.solve(expr, x)
        return result
    elif mode == 1 or 3:
        result = sympy.simplify(expr)
        return result




