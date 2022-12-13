# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
#  Порядок элементов менять нельзя.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

nums = "1, 5, 2, 3, 4, 6, 1, 7".split(',')
nums = list(map(int, nums))

def subsequence_create(nums: list) -> list:
    sub = []
    minimal = min(nums)
    sub.append(minimal)
    for i in range(nums.index(min(nums)), len(nums)):
        if nums[i] > minimal:
            sub.append(nums[i])
            minimal = nums[i]
    return sub

print(subsequence_create(nums))