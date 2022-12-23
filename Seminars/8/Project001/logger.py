from datetime import datetime as dt

def log_result(expr, result, mode):
    eventtime = dt.now().strftime('%d-%m %H:%M')
    
    if mode == 1:
        action = "Arithmetic operations"
    elif mode == 2:
        action = "Solution of the equations"
    elif mode == 3:
        action = "Symplifying polynomials"

    with open('calclog.cvs', 'a') as file:
        if mode == 1:
            file.write('{}; {}; {} = {}\n'
                    .format(eventtime, action, expr, result))
        elif mode == 2:
            file.write('{}; {}; {}; Roots: {}\n'
                    .format(eventtime, action, expr, result))
        elif mode == 3:
            file.write('{}; {}; {}; Symplyfied polynomial: {}\n'
                    .format(eventtime, action, expr, result))
