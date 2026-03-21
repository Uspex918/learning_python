# import math

# print("Программа калькулятор площади фигур")
# print(
#     'Введите:\n"s" - для квадрата\n"r" - для прямоугольника\n"c" - для круга\n"d" - для длины окружности'
# )

# choiсe = input("Ваш выбор: ")

# if choiсe == "s":
#     side = float(input("Введите длину стороны квадпата: "))
#     area = side**2
#     print("Площадь квадрата: " + str(area))
# elif choiсe == "r":
#     length = float(input("Введите длину прямоугольника: "))
#     width = float(input("Введите ширину прямоугольника: "))
#     area = length * width
#     print("Площадь рпямоугольника: " + str(area))
# elif choiсe == "c":
#     radius = float(input("Введите радиус круга: "))
#     area = math.pi * radius**2
#     print("Площадь круга: " + str(area))
# elif choiсe == "d":
#     radius = float(input("Введите радиус круга: "))
#     area = 2 * math.pi * radius
#     print("Длина окружности круга: " + str(area))
# else:
#     print("Ошибка: неверный ввод, попробуйте снова.")


# print("Программа калькулятор")

# num1 = float(input("Введите первое число: "))
# operation = input("Введите операцию (+, -, *, /): ")
# num2 = float(input("Введите второе число: "))

# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     if num2 != 0:
#         result = round(num1 / num2, 2)
#     else:
#         result = "Ошибка: деление на ноль!"
# else:
#     result = "Ошибка: неверная операция!"

# print("Ответ: " + str(result))


# num1 = float(input("Введите первое число: "))
# operation = input("Введите операцию (+, -, *, /): ")
# num2 = float(input("Введите второе число: "))


# message = "Ответ: "
# result = None

# if operation == "/":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         message = "Ошибка: деление на ноль!"
# elif operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# else:
#     message = "Ошибка: неверная операция!"

# if result == None:
#     print(message)
# else:
#     print(message, result)


# print("Конвертер валют")

# usd_to_pln = 4.0
# eur_to_pln = 4.3

# amount = float(input("Введите сумму: "))
# currency = input('Введите валюту ("usd" или "eur"): ')

# if currency == "usd":
#     result = amount * usd_to_pln
#     print(f"{str(amount)} USD = {str(result)} PLN")
# elif currency == "eur":
#     result = amount * eur_to_pln
#     print(f"{str(amount)} EUR = {str(result)} PLN")
# else:
#     print("Ошибка: неизвестная валюта")


print("Конвертер валют")

value = input("Из какой валюты нужно конвертировать:\n[CAD, USD, EUR]\n- ").upper()
amount = float(input("Введите сумму, которую вы хотите конвертировать: "))
value_con = input("В какую валюту конвертируем?:\n[CAD, USD, EUR]\n- ").upper()

CAD = 1
USD = 1.36
EUR = 1.6

exchange_to = value + "/" + value_con

if exchange_to == "CAD/USD":
    result = amount * (CAD / USD)
elif exchange_to == "USD/CAD":
    result = amount * (USD / CAD)
elif exchange_to == "CAD/EUR":
    result = amount * (CAD / EUR)
elif exchange_to == "EUR/CAD":
    result = amount * (EUR / CAD)
elif exchange_to == "USD/EUR":
    result = amount * (USD / EUR)
elif exchange_to == "EUR/USD":
    result = amount * (EUR / USD)
elif value == value_con:
    result = amount
else:
    result = None  # на случай неправильной пары

print("Результат операции:")
if result == None:
    print("Такой пары для обмена нет.")
else:
    print("Результат:", round(result, 2), value_con)
