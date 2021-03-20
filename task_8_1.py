# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен
# из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Уточнение
# Текст до собаки (Local-part): латинские буквы, цифры и символы: ' . _ + -
#
# Текст после собаки (Domain part): латинские буквы, цифры и символы . -
# 
# В Domain part обязательно должна быть хотя бы одна точка.
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

#(\w[a-z'._+-]*)\@(\w[a-z'.-]*) - не плохой

def email_parse(email):
# с ValueError
    email_pars_new = "(\w[a-z'._+-]*)\@((\w[a-z'.-]*)\.\w+)"
    huhd = re.fullmatch(email_pars_new, email)
    if huhd is None:
        raise ValueError
    huhd = huhd.groups()
    return {'username': huhd[0], 'domain': huhd[1]}

    #без .groups()
    #return {'username': huhd[1], 'domain': huhd[2]}

# без ValueError
# def email_parse(email):
#     parse_dict = {}
#     email_pars_new = re.compile(r"(\w[a-z'._+-]*)\@((\w[a-z'.-]*)\.\w+)")
#     huhd = email_pars_new.findall(email)
#     for i in huhd:
#         parse_dict['username'] = i[0]
#         parse_dict['domain'] = i[1]
#     return parse_dict

print(email_parse('someone@geekbrains.ru'))

#для проверки
#print(email_parse('someone@geekbrainsru'))

print(email_parse('sere.gas-chukin@mail.ru'))
