# 1'. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

num = str(input('Введите число: '))
point = num.find(".")
if point > -1:
    strnum = num.replace('.', '')
else:
    strnum = num.replace(',', '')
list = []
for i in range(len(strnum)):
    element = int(strnum[i])
    list.append(element)
print(f'Сумма цифр числа {num} - {sum(list)}')