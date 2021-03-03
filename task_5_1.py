#1. Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield, полностью истощить генератор. Например:

# gen1 = iterator_without_yield(11)
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
# File "<input>", line 1, in <module>
# StopIteration

n = int(input('Введите число для последоввательности: '))

iterator_without_yield = (num for num in range(1, n + 1, 2))
#print(type(iterator_without_yield))
print('Нечётные числа', *iterator_without_yield)
