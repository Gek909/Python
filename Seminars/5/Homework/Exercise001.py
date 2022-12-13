# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота
import random


def get_choice_of_first_pl():
    global count
    choice = int(input('Ход первого игрока. Введите количество конфет: '))
    while choice < 1 or choice > 28:
        print("Неверное количество конфет. Повторите ввод:")
        choice = int(input('Ход первого игрока. Введите количество конфет: '))
    count = count - choice
    print(f'Остаток конфет: {count}')
    return choice

def get_choice_of_second_pl():
    global count
    choice = int(input('Ход второго игрока. Введите количество конфет: '))
    while choice < 1 or choice > 28:
        print("Неверное количество конфет. Повторите ввод:")
        choice = int(input('Ход второго игрока. Введите количество конфет: '))
    count = count - choice
    print(f'Остаток конфет: {count}')
    return choice

    
def find_first_player():
    choice = int(input('Первый игрок, выбери цифру 1 или 0: '))
    chance = random.randint(0, 1)
    if choice == chance:
        print("Первый игрок ходит первым")
        print(f'Остаток конфет: {count}')
        return True
    else:
        print("Второй игрок ходит первым")
        print(f'Остаток конфет: {count}')
        return False

count = 117

if find_first_player() == True:
    while count > 28:
        if count > 28:
            get_choice_of_first_pl()
            if count <= 28:
                print("Второй игрок победил")

        if count > 28:
            get_choice_of_second_pl()
            if count <= 28:
                print("Первый игрок победил")

else:
    while count > 28:
        if count > 28:
            get_choice_of_second_pl()
            if count <= 28:
                print("Первый игрок победил")

        if count > 28:
            get_choice_of_first_pl()
            if count <= 28:
                print("Второй игрок победил")







