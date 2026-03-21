x = 5
y = 7

if x >= 0 and y >= 0:
    print(x * y)

name = "Alex"
if name and len(name) > 2:
    print("Имя непустое и длиннее двух символов")
x = 5
if x >= 1 and x < 10:  #
    print("x в диапазоне 1..9")
a = 10
b = 0
if b != 0 and a / b > 1:  # правая часть НЕ выполнится!
    print("Не будет деления на ноль")


username = ""
user = username or "Гость"  # если пустая строка > "Гость"
print(user)

age = 15
if age < 12 or age > 150:
    print("Возраст вне нормальных значений")

(True and False) or True  # > True
(True and "") or "fallback"  # > "fallback"
a = 0
b = 5
result = (a and b) or 100
print(result)  # > 100


data = ("" or 5) or 0
print(data)

0 and print("Не выполнится")  # > 0    (вызов print это тоже выражение)
"hi" or print("Не выполнится")  # > "hi"

name = ""
greeting = (name and "Hello " + name) or "Привет, гость!"
print(greeting)
