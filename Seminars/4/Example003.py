# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# *' 4 5 -> 20
# *' 6 3 -> 6
# *' 7 11 -> 77
# *' 6 8 -> 24

num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))

def findNOK(num1, num2):
    i = 2
    while i > 0:
        if (i % num1 == 0) and (i % num2 == 0):
            break
        else:
            i = i+1
    return i

print(findNOK(num1,num2))
