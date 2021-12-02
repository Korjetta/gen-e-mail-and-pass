import re
import random
import string

# функция создания почтовых адресов
def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

# функция генерации пароля
def parol():
    return (''.join(
        random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for i in
        range(12)))

filtered_lines = []
nameAndFamily = []
garbage = []

try:

    task_file_1 = open("task_file_1.txt.", "r")

    garbage = open("garbage.txt", "w")
    for line in task_file_1:
        if re.match(",\s[A-Z][a-z]+,\s[A-Z][a-z]+,\s[0-9]+,\s[A-Z][a-z]+(.[A-Z][a-z]+)?", line):


            nameSet = line.split(', ')
            nameAndFamily.append([nameSet[1], nameSet[2]])
            filtered_lines.append(line.replace('\n', '') + ", " + parol() + '\n')
        else:

            garbage.write(line)
    garbage.close()
    task_file_1.close()

    