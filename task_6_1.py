# 1. Не используя библиотеки для парсинга,
# распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание:
# - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# - Вы не знате заранее насколько идентичен шаблон строк файла. Попробуйте оценить это.

with open('copi_6_1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lists = []
        #print(line)
        #print(type(line))
        split_line = line.split(' ')
        remote_addr = split_line[0]
        lists.append(remote_addr)
        request_type = split_line[5][1:]
        lists.append(request_type)
        requested_resource = split_line[6]
        lists.append(requested_resource)
        tuple_parsing = tuple(lists)
        print(tuple_parsing)
