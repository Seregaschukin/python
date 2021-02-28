#2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.


from requests import get, utils

def currency_rates(currensy):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    #print(type(content))
    find_curr = content.find(currensy)
    if currensy in content:
        interval = find_curr + 200
        new_str = content[find_curr:interval]
        find_new_str = new_str.find('<Value>')
        start_find = find_new_str + 7
        finish_find = start_find + 7
        print_find_currensy = new_str[start_find:finish_find]
        currensy_float = float(print_find_currensy.replace(',', '.'))
        #print(type(currensy_float)) #Подтверждение типа float
        return currensy_float
    else:
        return None

currensy = input('Введите индекс валюты: ').upper()
print(f'{currency_rates(currensy)} RUB за 1 единицу {currensy}')
