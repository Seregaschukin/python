max_number = 1000
min_number = 0
even_number = 0
digits_of_number = 0
while min_number < max_number:
    if min_number % 2:
        even_number = min_number
        digits_of_number = even_number ** 3
        idx = 1
        sum_digits_of_number = 0
        percent = 10
        sum_digits = 0
        while digits_of_number >= idx:
            sum_digits_of_number = digits_of_number // idx % percent
            idx *= 10
            sum_digits += sum_digits_of_number
        if sum_digits % 7 == 0:
            print('Нечетное число возведенное в куб - ', digits_of_number)
            print('Сумма чисел данного числа', sum_digits)
            print()
    min_number += 1
