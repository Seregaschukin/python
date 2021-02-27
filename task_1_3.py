declensions = ['процент', 'процента', 'процентов']
utu = []
user_number = int(input('Введите число от 0 до  20: '))
for declensions_number in declensions:
    if user_number == 1:
        declensions_number = 0
        utu = declensions[declensions_number]
    elif 1 < user_number < 5:
        declensions_number = 1
        utu = declensions[declensions_number]
    else:
        declensions_number = 2
        utu = declensions[declensions_number]
print(user_number, utu)

print()
print('Все склонения:')

declensions = ['процент', 'процента', 'процентов']
min_number = 0
for idx, item in enumerate(declensions, start = 0):
    while min_number <= 20:
        if min_number == 1:
            number_declensions = 0
        elif 1 < min_number < 5:
            number_declensions = 1
        else:
            number_declensions = 2
        min_number += 1
        print(idx, '-', declensions[number_declensions])
        idx += 1