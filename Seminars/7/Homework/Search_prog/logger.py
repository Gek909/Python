def get_data():
    with open('Phonebook.txt', 'r') as file:
        base = file.read().split('\n')
        return base
