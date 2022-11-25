# Квадрат числа
# a = int(input('a = '))
# print(a**2)







# Программа, которая проверяет, является ли одно число квадратом другого:

# a = int(input('a = '))
# b = int(input('b = '))
# if a == b**2 or b == a**2:
#     print('Одно число является квадратом другого')
# else:
#     print('Ни одно число не является квадратом другого')








# Программа, которая на вход принимает 5 чисел и находит максимальное из них.

# a = input().split()
# max = int(a[0])
# for i in range(len(a)):
#     if int(a[i]) > max:
#         max = int(a[i])
# print(max)

# Лучший вариант:

# a = list(map(int,input().split()))
# print(max(a))







# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# a = int(input('a = '))
# for i in range(-a,a+1):
#     print(i, end = ' ')


# 2 версия
# n = int(input())
# a = []
# for i in range (-n,n+1):
# 	a.append(i)
# print(a)


# 3 версия
# n = int(input())
# a = []
# b = ''
# for i in range (-n,n+1):
# 	a.append(i)
# 	b += f' {i} '
# print(b)



# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.

# res = float(input('num = '))  # 123.5232
# res = int((res*10)%10)
# print(res)



# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно ((5 и 10) или 15), но не 30.

num = int(input('num = '))
if num % 30 == 0:
    print('No')
elif num % 15 == 0 or (num % 5 == 0 and num % 10 == 0):
    print('Yes') 
else:
    print('No')
