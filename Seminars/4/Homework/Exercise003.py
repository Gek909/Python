# 3'. Задайте последовательность чисел. Напишите программу, которая выведет
#  список неповторяющихся элементов исходной последовательности.

nums = [2, 4, 1, 4, 2, 0, 4, 2, 1, 4]
new_nums = []
[new_nums.append(i) for i in nums if i not in new_nums]

print(nums)
print(f'Неповторяющиеся элементы исходной последовательности: {new_nums}')