# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
#
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
#
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


#вывод через запятую в одну строку
def type_logger(func):

    def wrepper(*args, **kwargs):
        print(", ".join([f"{i}: {type(i)}" for i in args]))
        print(", ".join([f"'{key}' = {val}: {type(val)}" for key, val in kwargs.items()]))
        result = func(*args)
        return result
    return wrepper

#вывод построчно
# def type_logger(func):
#     def wrepper(*args, **kwargs):
#         for i in args:
#             print(f'{i}: {type(i)}')
#
#         for val, key in kwargs.items():
#             print((f'{val} = {key} : {type(key)}'))
#
#         result = func(*args)
#         return result
#
#     return wrepper

#вывод списком через запятую
# def type_logger(func):
#     def wrepper(*args, **kwargs):
#         spisok = []
#         for i in args:
#             spisok.append(f'{i}: {type(i)}')
#
#         for val, key in kwargs.items():
#             spisok.append(f'{val} = {key} : {type(key)}')
#
#         print(spisok)
#
#         result = func(*args)
#         return result
#
#     return wrepper

@type_logger
def calc_cube(*args):
   return args

calc_cube(5,2,'ghfg', {5:6})
calc_cube('ghfg')
calc_cube(calc_cube)
calc_cube(1, a=2.3, b=True, c="q")
