# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из
# трех случайных слов, взятых из трёх списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
from random import choice

def get_jokes(max_jokes, nouns, adverbs, adjectives):
    """
    :param max_jokes: Number of jokes
    :param nouns:the first word of the joke
    :param adverbs:the second word of the joke
    :param adjectives:the third word of the joke
    :return: jokes
    """
    #Возьмем из каждого списка по 1 слову при помощи ранее импортированного модуля, выйдем из вайл по условию
    n = 0
    jokes = []
    while n < max_jokes:
        jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n += 1
    return jokes

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

max_jokes = int(input('Введите количество шуток: '))
get_jokes(max_jokes, nouns, adverbs, adjectives)
print(get_jokes(max_jokes, nouns, adverbs, adjectives))
