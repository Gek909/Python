# '1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81


# num = int(input('Введите число: '))
# list = []
# list.append(1)
# for i in range(1, num):
#     res = list[i-1] * -3
#     list.append(res)
# print(list)






# '2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}





# num = int(input('Введите число: '))
# dictionary = {}
# for i in range(1, num+1):
#     dictionary[i] = int(3*i+1)
# print(dictionary)







# '3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# str1 = input('Введите 1ую строку: ')
# str2 = input('Введите 2ую строку: ')
# if len(str1) >= len(str2):
#     exist = str1.count(str2)
#     print(f'Количество вхождений строки 2 в строку 1: {exist}')
# elif len(str1) < len(str2):
#     exist = str2.count(str1)
#     print(f'Количество вхождений строки 1 в строку 2: {exist}')
    
    
# вариант 2 - без использования встроенных методов.

a = input()
b = input()
count = 0
for i in range(len(a)):
    if a[i:i+len(b)] == b:
        count += 1
print(count)
print(a.count(b))