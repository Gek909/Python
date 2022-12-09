# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1) с помощью математических формул нахождения корней квадратного уравнения

# 2) с помощью дополнительных библиотек Python(дополнительный sympy,scipy)
import math
def findDisc(a, b, c):
    disc = b**2 - 4 * a * c
    return disc
disc = findDisc(5, 24, -5)
def solve(a, b, disc):
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2*a)
        x2 = (-b - math.sqrt(disc)) / (2*a)
        result = f'x1 = {x1}, x2 = {x2}'
    elif disc == 0:
        x = -b/(2*a)
        result = f'x = {x}'
    elif disc < 0:
        result = "Корней нет"
    return result

print(solve(5, 24, disc))
