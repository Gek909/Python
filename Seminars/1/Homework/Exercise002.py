x = int(input('Введите X: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))

if (not(x or y or z)) == (not x and not y and not z):
    print('True')
else:
    print('False')
