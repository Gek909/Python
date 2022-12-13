# Задано N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
#  чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# *' 1 2 3 4 6 7 -> 5
# *' 1 3 -> 2
# *' 3 4 6 7 8 -> 5

# TODO 1:16:54

nums = "1 2 3 4 5 6".split()
nums = list(map(int, nums))

def subsequence_check(nums: list) -> int:
    try:
        for i in range(len(nums)+1):
            if nums[i] != nums[i+1]-1:
                print(int(nums[i]+1))
                break
    except:
        print('Последовательность не нарушена')

subsequence_check(nums)

    