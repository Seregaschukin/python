# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом
# — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка
# — один пользователь, разделитель между значениями — запятая. Написать код,
# загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
#
#     Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
#     то для оставшихся ФИО значение в словаре - None.
#     Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
#     Примечание: При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
#
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи
import json
import pickle

with open('users.csv', 'r', encoding='utf-8') as f:
    line_user = f.readline()
    list_user = []
    while line_user:
        line_user_str = line_user.strip() #print(line_user_str)
        line_user_sp = line_user_str.split(',') #print(line_user_sp)
        line_user_join = ' '.join(line_user_sp) #print(line_user_join)
        list_user.append(line_user_join)
        line_user = f.readline() #print(list_user)

with open('hobby.csv', 'r', encoding='utf-8') as f:
    line_hobby = f.readline()
    list_hobby = []
    while line_hobby:
        line_hobby_str = line_hobby.strip()
        line_hobby_sp = line_hobby_str.split(',')
        line_hobby_join = ' '.join(line_hobby_sp) #print(line_hobby_join)
        list_hobby.append(line_hobby_join)
        line_hobby = f.readline() #print(list_hobby)

print(f'Список с ФИО: {list_user}')
print(f'Список с хобби: {list_hobby}')


for i in list_user:
    if len(list_user) > len(list_hobby):
        list_hobby.append(None)
print(f'Новый список с хобби: {list_hobby}')

new_dict = dict(zip(list_user, list_hobby))
print(new_dict)

with open('user_hobby.txt', 'w', encoding='utf-8') as f:
    en_dict = str(new_dict).encode(encoding='utf-8')
    de_dict = en_dict.decode(encoding='utf-8')
    f.write(de_dict)
