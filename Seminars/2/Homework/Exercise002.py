# 2'. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math

num = int(input('Введите число: '))
list = []
for i in range(0, num):
    res = math.factorial(i+1)
    list.append(res)
print(f'Факториалы чисел от 1 до {num}: \n{list}')