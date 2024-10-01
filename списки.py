r = int(input('Введи довжину списка: '))

user_list = []

i = 0
while i < r:
    string = 'Введи номер елементу №' + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)