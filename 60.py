# count = 0

# while count < 5:
#     print(count)
#     count += 1

# print(count)


while True:
    password = input("Введите пароль:\n")
    if len(password) >= 8:
        break
    print("Пароль должен быть как минимум из 8 символов")


print(password)
