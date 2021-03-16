# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os
from os.path import join

main_dirs = 'my_project'

new_dict = {}
list_ten = []
list_hun = []
list_th = []
list_ten_th = []

for root, dirs, files in os.walk(main_dirs):
    for file in files:
        size = os.stat(join(root, file)).st_size
        #print(size)
        if 0 <= size < 10:
            list_ten.append(size)
            len_cou_ten = len(list_ten)
            new_dict[10] = len_cou_ten
        elif 10 <= size < 100:
            list_hun.append(size)
            len_cou_hun = len(list_hun)
            new_dict[100] = len_cou_hun
        elif 100 <= size < 1000:
            list_th.append(size)
            len_cou = len(list_th)
            new_dict[1000] = len_cou
        elif 1000 <= size < 10000:
            list_ten_th.append(size)
            len_cou = len(list_ten_th)
            new_dict[10000] = len_cou
        elif 10000 <= size < 100000:
            list_ten_th.append(size)
            len_cou = len(list_ten_th)
            new_dict[100000] = len_cou

print(new_dict)
