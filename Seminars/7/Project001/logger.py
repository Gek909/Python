from datetime import datetime as dt

def log_result(mode, result):
    eventtime = dt.now().strftime('%d-%m %H:%M')
    
    if mode == 1:
        game = "Крестики-нолики"
    else:
        game = "Конфеты"

    with open('gamelog.cvs', 'a') as file:
        if result != "Ничья":
            file.write('{}; {}; {} победил\n'
                    .format(eventtime, game, result))
        else:
            file.write('{}; {}; {}\n'
                    .format(eventtime, game, result))
