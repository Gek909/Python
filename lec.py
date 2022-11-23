# print('hello world')

# value = None
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# value = 12344
# # print(type(value))
# s = 'Hello world'
# print(s)
# print (a, '-', b, '-', s)
# print ('{1} - {2} - {0}'.format(a,b,s))
# print (f'{a} - {b} - {s}')
# 
# f = True
# print(f)


# list = []
# list = ['1','2','3', 'hello', 1, 2, 4.5, True]
# print(list)


# Ввод и вывод данных

# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a, '+' , b, ' = ', a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')


# Арифметические операции

# a = 123
# b = 321
# c=a+b
# print(c)


# Логические операции

# func = 1
# T = 4
# x = 123

# print(func<T>(x))
# 
# f = 1>2 or 4<6
# 
# print(f)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)
# 
# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции IF, IF-ELSE

# a = int(input('a = '))
# b = int(input('b = 2'))
# if a>b:
#     print(a)
# else:
#     print(b)

#  WHILE

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй хватит')
# print(inverted)

# Управляющие конструкции FOR

# for i in range(1, 5):
#     print(i)


# НЕМНОГО О СТРОКАХ

# text = 'съешь ещё этих мягких французских булок'
# 
# 
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #

# ФУНКЦИИ

# def f(x):
#    return x**2

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

    
arg = 1
print(f(arg))


#print(f(1)) # Целое
#print(f(2.3)) # 23
#print(f(28)) # None
#print(type(f(1))) # str
#print(type(f(2.3))) # int
#pr