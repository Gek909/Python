# 1'. Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415


import math

d = float(input('Введите число d: '))

def find_count(d):
    count = 0
    while d < 1:
        d = d*10 
        count += 1
    return int(count)
    
p = round(float(math.pi), find_count(d))
print(f'Число ПИ при заданной точности: {p}')