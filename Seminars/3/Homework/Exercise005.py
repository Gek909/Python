# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. (Дополнительное)

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(-10)
# for i in range(1,n):
#     print(f'{fibonacci(i)}')

# def fibo(n):
#     if n = 1
# f(-n) = (-1)**(n+1)*f(n)
# print(f(5))

num = int(input('Введите число: '))
fibo = [0, 1, 1]
fib1 = 0
fib2 = 1
fib3 = 1
i = 0
while i < num - 2:
    fib_sum = fib2 + fib3
    fib2 = fib3
    fib3 = fib_sum
    i = i+1
    fibo.append(fib3)

negafibo = [1, -1]
negafib1 = 1
negafib2 = -1
j = 0
while j < num - 2:
    negafib_sum = negafib1 - negafib2
    negafib1 = negafib2
    negafib2 = negafib_sum
    j = j+1
    negafibo.append(negafib2)

negafiboreversed = list(reversed(negafibo))
result = negafiboreversed + fibo
print(result)