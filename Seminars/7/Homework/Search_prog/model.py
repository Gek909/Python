def find_contact(object, base):
    results = []
    object = object.lower()
    for i in range(len(base)):
        temp = base[i].lower()
        if temp.find(object) >= 0:
            results.append(i)
    return results    

def create_contact(object):
    with open('Phonebook.txt', 'a') as file:
            file.write(f'{object}\n')
