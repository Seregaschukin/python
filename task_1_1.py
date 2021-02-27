duration = int(input('Введите время в секундах: '))
minute = 60
hour = 60 * 60
day = 60 * 60 * 24

if duration < minute:
    print(duration, 'сек')
elif minute <= duration < hour:
    print(duration // minute, 'мин', duration % minute, 'сек')
elif hour <= duration < day:
    print(duration // hour,  'час', duration // minute % minute, 'мин', duration % minute, 'сек' )
else:
    print(duration // day, 'дн', duration % day // hour, 'час', duration // minute % minute, 'мин', duration % minute, 'сек')
    #ff

