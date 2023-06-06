# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", "r") as file:
    list_of_lines = file.readlines()
    list_of_checks = []
    sum_of_prices = 0
    for price in list_of_lines:
        price = ''.join([i for i in price if i.isdigit()])
        if price == '':
            list_of_checks.append(sum_of_prices)
            sum_of_prices = 0
        else:
            sum_of_prices += int(price)
    list_of_checks.append(sum_of_prices)

three_most_expensive_purchases = sum(sorted(list_of_checks)[-3:])


assert three_most_expensive_purchases == 202346