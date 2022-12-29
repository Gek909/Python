import random

def find_first_player():
    chance = random.randint(0, 1)
    if chance == 0:
        return "Игрок"
    else:
        return "Бот"
