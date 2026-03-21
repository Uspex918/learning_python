# # 1 задача
# number = float(input("Введите число: "))

# if number == 0:
#     print(f"число равно {number}")
# elif number < 0:
#     print(f"число {number} отрицательное")
# else:
#     print(f"число {number} положительное")

# # 2 задача
# age = int(input("Введите возраст: "))

# if age < 0 or age > 150:
#     print("Не валидный диапазон!")
# elif age <= 12:
#     print("Ребёнок (до 12)")
# elif age <= 17:
#     print("Подросток (13–17)")
# else:
#     print("Взрослый (18 и старше)")


# # 3 задача
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))

# if a == b:
#     print("Числа равны")
# elif a > b:
#     print(a)
# else:
#     print(b)


# # 4 задача
# temp = float(input("Введите температуру: "))

# if temp < 10:
#     print("Холодно")
# elif temp <= 24:
#     print("Тепло")
# else:
#     print("Жарко")


# # 5 задача
# num = int(input("Введите число: "))

# if num % 2 == 0:
#     print("Четное")
# else:
#     print("Не четное")


# # 6 задача
# password = input("Введите пароль: ")

# if len(password) < 6:
#     print("Слишком короткий пароль")
# else:
#     print("Пароль принят")

# # задача 7
# score = int(input("Введите оценку: "))

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# # задача 8
# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))

# if b == 0:
#     print("На 0 делить нельзя")
# elif a % b == 0:
#     print("Кратно")
# else:
#     print("Не кратно")


# # задача 9
# num = float(input("Введите число: "))

# if 0 < num < 100:
#     print(round(num, 2))
# else:
#     print("Только от 0 до 100")


# # задача 10
# text = input("Введите строку: ")

# if len(text) > 10:
#     print("Длинная строка")
# else:
#     print("Короткая строка")


# # задача 11
# a = float(input("Часть: "))
# b = float(input("От целого: "))

# if b == 0:
#     print("На ноль делить нельзя! И части от 0 нет.")
# else:
#     percent = round((a / b) * 100, 2)

# print(percent)


# # задача 12
# num = float(input("Введите число: "))
# rounding = int(input("До какого знака округлять: "))

# if rounding < 0:
#     print("Значение для количсетва знаков после точки не может быть меньше 0")
# else:
#     print(round(num, rounding))

# # задача 13
# num = input("Введите число: ")

# if "." in num:
#     num = float(num)
# else:
#     num = int(num)

# print(num)


# # задача 14
# a = float(input("Введите число: "))
# b = float(input("Введите 2-е число: "))353

# if b == 0:
#     print("На 0 делить нельзя")
# else:
#     print(a / b)


# # аздача 15
# name = input("Введите Имя: ")
# last_name = input("Введите Фамилию: ")

# if " " in name:
#     print("Вводите имя и фамилию раздельно")
# elif not name.strip() or not last_name.strip():
#     print("Имя или фамилия пустые")
# else:
#     print(f"Вас зовут {name} {last_name}")


url = "example.com"

if "https://" not in url and "www." not in url:
    url = "https://" + "www." + url
elif "https://" not in url and "www." in url:
    url = "https://" + url

print(url)
