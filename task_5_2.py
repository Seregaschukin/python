#2. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield. Полностью истощить генератор. Например:
#
# gen1 = iterator_with_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


def iterator_with_yield(nums):
    for num in range(1, nums + 1, 2):
        yield num


nums = int(input('Введите число для последоввательности: '))
new_gen = iterator_with_yield(nums)
for i in new_gen:
    print('Нечётные числа:', i)
print('Генератор истощен')

#Повторное использование функции
# new_gen = iterator_with_yield(6)
# for i in new_gen:
#     print('Нечётные числа:', i)
#
# #print(type(new_gen))
# print('Генератор истощен')
