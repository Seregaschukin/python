# 4. Представлен список чисел. Необходимо вывести те его элементы,
# значения которых больше предыдущего, например:
#
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
# Выводит или не выводить первый элемент - решите сами.
# Используйте генераторы или генераторные выражения.
#
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#print(type(src))
#print(src[0])

def more_than_previous_one(src):
    len_src = 0
    i = 0
    j = 1
    new_src = []
    while len_src <= len(src) and j < len(src):
        if src[i] < src[j]:
            new_src.append(src[j])
        i += 1
        j += 1
        len_src += 1
    yield new_src

new_gen = more_than_previous_one(src)
for i in new_gen:
    print(i)
print(type(new_gen))
