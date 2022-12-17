import controller

def choose_mode():
    return int(input('Выберите игру - 1 = "Крестики-нолики", 2 = "Конфеты: '))

def show_result(result):
    if result != "Ничья":
        print(f'{result} победил ')
    else:
        print(result)

