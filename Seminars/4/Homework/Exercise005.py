# 5'. Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
import sympy

with open('HW4_Ex5File1.txt', 'r') as file1:
    first_polynominal = file1.read()

with open('HW4_Ex5File2.txt', 'r') as file2:
    second_polynominal = file2.read()

print(first_polynominal)
print(second_polynominal)

a = first_polynominal
b = second_polynominal
print(sympy.simplify(a + '+' + b))

with open('HW5_Ex5Polys_sum.txt', 'w') as file:
    file.write(str(sympy.simplify(a + '+' + b)))