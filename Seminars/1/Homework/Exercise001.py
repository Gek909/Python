num = int(input('Введите число, соответствующее дню недели: '))
if num in range(1,6):
    print('Будний день')
elif num in range(6,8):
    print('Выходной')
else:
    print('Введите число от 1 до 7')