def del_abv_elem(message):
    part = 'абв'
    new_text = [word for word in message.split() if part not in word]
    answer = (" ".join(new_text))
    return answer


