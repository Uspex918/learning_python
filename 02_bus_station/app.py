# count = 0
# text = "left or right"

# text += "!"

# print(count)
# print(text)

import math
from turtle import reset

num_tickets = 237  # количество проданных билетов
bus_capacity = 48  # количество мест в автобусе

# Ваше решение:
# buses_num = num_tickets // bus_capacity
# rest_of = num_tickets % bus_capacity

buses_num = math.floor(num_tickets / bus_capacity)
buses_need = math.ceil(num_tickets / bus_capacity)
rest_of = num_tickets - (buses_num * bus_capacity)

# Замените None в функции print на переменные с результатом,
# чтоб можно было проверить при помощи теста.
# Первый - количество автобусов
# Второй - оставшееся количество пассажиров (купленных билетов)
print(buses_num, buses_need, rest_of)
