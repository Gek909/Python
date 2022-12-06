# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке некое число.
# Пример:
# ['114411', 'sjngsjgng', '123fsghs'] -> No
# ['12', 12] -> Yes

# 1 вариант
# list = ['114411', 'sjngsjgng', '123fsghs']
# count = 0
# for i in range(len(list)):
#     if isinstance(list[i], int) or isinstance(list[i], float):
#         count += 1
# if count == 0:
#     print("No")
# else:
#     print("Yes")

# 2 вариант
mass = [114411, 'sjngsjgng', '123fsghs']
types = [str(type(i)) for i in mass]
if "<class 'int'>" in types or "<class 'float'>" in types:
    print('Yes')
else:
    print('No')