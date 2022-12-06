# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))
temp = num
result = ""
while temp > 0:
    result = str(int(temp%2)) + result
    temp = int(temp / 2)
print(f'Число {num} в двоичной системе: \n{result}')