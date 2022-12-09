# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)

# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5
import random

k = int(input('Введите число степени k: '))

def random_polynominal_generate(k):
    ch = '0'
    i = 0
    temp = k
    result = ""
    while i < k + 1:
        if i < k - 1:
            elem = str(random.randint(0, 100)) + "*x^" + str(temp) + " + "
            if elem.find(ch) != 0:
                result = str(result) + str(elem)
                temp = temp - 1
                i = i + 1
            else:
                result = str(result)
                temp = temp - 1
                i = i + 1
        elif i == k - 1:
            elem = str(random.randint(0, 100)) + "*x" + " + "
            if elem.find(ch) != 0:
                result = str(result) + str(elem)
                temp = temp - 1
                i = i + 1
            else:
                result = str(result)
                temp = temp - 1
                i = i + 1
        elif i == k:
            elem = str(random.randint(0, 100))
            if elem.find(ch) != 0:
                result = str(result) + str(elem)
                temp = temp - 1
                i = i + 1
            else:
                result = str(result)
                temp = temp - 1
                i = i + 1
    return result

with open('HW4_Ex4.txt', 'w') as file:
    file.write(random_polynominal_generate(k))

