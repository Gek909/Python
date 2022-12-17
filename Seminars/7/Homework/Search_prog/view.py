import controller

def choose_mode():
    return int(input('1 = find contact; 2 = create new contact \nChoose action: '))

def get_object(mode):
    if mode == 1:
        return str(input('Input information to find: '))
    if mode == 2:
        return str(input('Input contact details. \nFormat: Surname Phone: '))

def show_result(results, base):
    for i in range(len(results)):
        print(base[results[i]])

def sucсessfullly_added(object):
    print(f'"{object}" successfully added to phonebook')