# 4. Создать список, содержащий цены на товары (10 – 20 товаров), например:
#
# [57.8, 46.51, 97, ...]
# - Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# - Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка
# после сортировки остался тот же).
# - Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# - Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price = [57.8, 46.51, 97, 45.6, 567, 0.47, 86, 84, 66, 5]

for cost in price:
    cost_rub = int(cost)
    cost_coin = round((cost-cost_rub)*100)

    if 0 < cost_coin < 10:
        cost_coin = f"0{cost_coin}"
    elif cost_coin == 0:
        cost_coin = f"00"
    else:
        cost_coin = f"{cost_coin}"
    print(f"{cost_rub} руб {cost_coin} коп", end=", ")
print("\nДоказательство операции in place:")
print(f"\tid перед сортировкой {id(price)}")
price.sort()
print(f"\tid после сортировки {id(price)}")
lst_descending = list(reversed(price))
print(f'Новый список по убыванию {lst_descending}')
print("5 самых дорогих товаров:")
for cost in lst_descending[:5]:
    print(f"\t{cost}")

