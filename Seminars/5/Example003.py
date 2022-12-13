# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

text = 'абвгд гдежз жзе абв ыопыпт'
text_list = text.split(' ')
part = 'абв'
new_text = []
for word in text_list:
    if part not in word:
        new_text.append(word)

new_str = (" ".join(new_text))

print((new_str))


# 2 вариант

# del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])

# print(del_st('абвгд гдежз жзе абв ыопыпт', 'абв'))