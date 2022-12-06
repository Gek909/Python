# 5'. Реализуйте алгоритм перемешивания списка.
import random
list = input('Введите элементы списка через пробел: ').split()

randomlist = []
randomindex = random.sample(range(0, len(list)), len(list))
for i in range(len(list)):
        randomlist.append(list[randomindex[i]])

print(f'Перемешанный список: \n{randomlist}')


# 2 вариант
# for i in range(len(mass)-1):
#         n = ranint(0, len(mass)-1)
#         mass[i], mass[n] = mass[n], mass[i]