# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки,содержащие
# имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
#
# Замечание: Заранее неизвестно сколько фамилий передадут в функцию thesaurus
# Подумайте: полезен ли будет вам оператор распаковки?
# Сможете ли вы вернуть отсортированный по ключам словарь?

def thesaurus(*args):
    thesaurus_dicts = dict()
    for vals in args:
        key = vals[:1]
        if key in thesaurus_dicts.keys():
            thesaurus_dicts[key].append(vals)
        else:
            thesaurus_dicts[key] = [vals]
    #return thesaurus_dicts #без сортировки

    sort_dict = dict()
    for key in sorted(thesaurus_dicts.keys()):
        sort_dict[key] = thesaurus_dicts[key]
    return sort_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Федя", "Антон", "Петр", "Илья"))
