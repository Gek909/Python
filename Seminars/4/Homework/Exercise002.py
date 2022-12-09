# 2'. Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

num = int(input('Введите число: '))

def find_multipliers(num):
    i = 2
    multipliers = []
    while num != 1:
        if num % i == 0:
            multipliers.append(i)
            num = num/i
        else:
            i += 1
    return multipliers
result = set(find_multipliers(num))
print(f'Простые множители числа {num}: {result}')
        
