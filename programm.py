import random

# функция создания почтовых адресов
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

# Функция генерации пароля
def parol():
    return (''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for i in
        range(12)))