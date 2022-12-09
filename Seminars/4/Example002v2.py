import sympy
# from sympy.solvers import solve
# from sympy import Symbol
 
# def fun(a,b,c):
#     x = Symbol('x')
#     return solve(f'{a}*x**2+{b}*x+{c}', x)
    
# print('Корни уравнения:', *fun(5, 24, -5)) 

# пример
x = sympy.Symbol('x')
b = 4*x**3 + 3*x**2 + x + 10
c = 8*x**9 + 3*x**2 + 9
print(sympy.simplify(b+c))
