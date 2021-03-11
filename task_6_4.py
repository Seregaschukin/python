# 4. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки:
# для записи данных и для вывода на экран записанных данных.
#
#     Данные хранить в файле bakery.csv в кодировке utf-8.
#
# При записи передавать из командной строки значение суммы продаж. Новая запись дозаписывается в конец файла.

# Для чтения данных реализовать в командной строке следующую логику. Предполагаем, что первая запись имеет номер 1.
# 1) просто запуск скрипта — выводить все записи;
# 2) запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# 3) запуск скрипта с двумя числами — выводить записи, начиная с номера,
# равного первому числу, по номер, равный второму числу, включительно;
#
# Примеры запуска скриптов:
#
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
#
# Усложнение Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

#add_sale.py
#первый скрипт
from sys import argv
print(argv)

if len(argv) < 2:
    print("Не передана сумма продаж")
    exit(1)

with open("bakery.csv", encoding="UTF-8", mode="at") as file:
    file.write(f"{argv[1]}\n")


#show_sales.py
#второй скрипт
from sys import argv

len_argv = len(argv)
with open("bakery.csv", encoding="UTF-8", mode="rt") as file:
    if len_argv == 1:
        print("Show all records:")
        for line in file:
            print(line.strip())
    elif len_argv == 2:
        record_begin = int(argv[1])
        print(f"Show records from record {record_begin}:")
        for idx, line in enumerate(file):
            if idx >= record_begin-1:
                print(line.strip())
    else:
        record_begin = int(argv[1])
        record_end = int(argv[2])

        print(f"Show records from record {record_begin}:")
        for idx, line in enumerate(file):
            if record_begin-1 <= idx <= record_end-1:
                print(line.strip())
