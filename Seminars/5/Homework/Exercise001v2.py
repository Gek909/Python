# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота


# Версия с ботом:
import random


def get_choice_of_player():
    global count
    choice = int(input('Ход игрока. Введите количество конфет: '))
    while choice < 1 or choice > 28:
        print("Неверное количество конфет. Повторите ввод:")
        choice = int(input('Ход игрока. Введите количество конфет: '))
    count = count - choice
    print(f'Остаток конфет: {count}')
    return choice

def get_choice_of_bot():
    global count
    choice = random.randint(1,28)
    count = count - choice
    print(f'Бот взял {choice} конфет(ы). Остаток конфет: {count}')
    return choice

    
def find_first_player():
    choice = int(input('Игрок, выбери цифру 1 или 0: '))
    chance = random.randint(0, 1)
    if choice == chance:
        print("Игрок ходит первым")
        print(f'Остаток конфет: {count}')
        return True
    else:
        print("Бот ходит первым")
        print(f'Остаток конфет: {count}')
        return False

count = 117

if find_first_player() == True:
    while count > 28:
        if count > 28:
            get_choice_of_player()
            if count <= 28:
                print("Бот победил")

        if count > 28:
            get_choice_of_bot()
            if count <= 28:
                print("Игрок победил")

else:
    while count > 28:
        if count > 28:
            get_choice_of_bot()
            if count <= 28:
                print("Игрок победил")

        if count > 28:
            get_choice_of_player()
            if count <= 28:
                print("Бот победил")







