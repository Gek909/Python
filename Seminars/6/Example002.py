# Задача 2.

# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))

# Ввод:
# house=дом car=машина men=человек tree=дерево
# Вывод:
# (('house', 'дом'), ('car', 'машина'), ('men', 'человек'), ('tree', 'дерево'))

dict = "house=дом car=машина men=человек tree=дерево"
dict = dict.replace('=', ' ')
dict = dict.split()

# dict = list(map(turples, dict))

dict = [(dict[i], dict[i+1]) for i in range(0, len(dict)-1, 2)]
dict = tuple(dict)

print(dict)

# Лучший вариант

# a = 'house=дом car=машина men=человек tree=дерево'.split()
# a = tuple(map(lambda x: tuple(x.split('=')),a))
# print(a)
