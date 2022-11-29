# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

with open('file.txt', 'r') as file:
    elems = file.read().split('\n')

for i in range(0, len(elems)):
    elems[i] = int(elems[i])

num = int(input('Введите число N: '))
list = []
for i in range(0, num*2+1):
    res = -num+i
    list.append(res)
print(f'Последовательность чисел от -{num} до {num}: \n{list}')

prod = 1
for i in range(len(elems)):
    prod = prod * list[elems[i]]
print(f'Произведение элементов на позициях {elems}:\n{prod}')