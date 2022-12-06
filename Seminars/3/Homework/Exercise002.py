# 2'. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
#    0  1  2  3  4
# - [2, 3, 5, 6] => [12, 15]

list = input('Введите элементы списка через пробел: ').split()
prod = 1
result = []
if len(list) % 2 == 0:
    for i in range(0, int(len(list)/2)):
        prod = int(list[i]) * int(list[len(list)-i-1])
        result.append(prod)
else:
    for i in range(0, int(len(list)/2)):
        prod = int(list[i]) * int(list[len(list)-i-1])
        result.append(prod)
    last_elem = int(list[int(len(list)/2)])**2
    result.append(last_elem)
print(result)
