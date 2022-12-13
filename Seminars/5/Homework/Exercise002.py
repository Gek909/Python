# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)

field = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def show_field():
    global field
    for i in range(0, len(field), 3):
        print(field[i], field[i+1], field[i+2])

def get_choice_of_first():
    choice = int(input('Ход первого игрока. Введите номер позиции: '))
    return choice

def get_choice_of_second():
    choice = int(input('Ход второго игрока. Введите номер позиции: '))
    return choice



def change_field(get_choice, field, show_field, ch):
    choice = int(get_choice())
    for i in range(0, len(field), 3):
        field[choice] = ch
        print(field[i], field[i+1], field[i+2])

show_field()
change_field(get_choice_of_first, field, show_field, "X")
change_field(get_choice_of_second, field, show_field, "O")
change_field(get_choice_of_first, field, show_field, "X")
change_field(get_choice_of_second, field, show_field, "O")






