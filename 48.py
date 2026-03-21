num1 = float(input("First num: "))
action = input("Enter operation sign: ")
num2 = float(input("Second num: "))

if action == "/":
    if num2 == 0:
        result = None
        message = "Cant divide by ziro!"
    else:
        result = num1 / num2
        message = ""
else:
    result = None
    message = "Not support operation with " + action + " sign!"

if result == None:
    print(message)
else:
    print("Answer is", result)


# x = 0

# if x == None:
#     print("Нет значения")

# print(bool([]) == False)

# a = "hello"
# b = "hello"
# a = "hello world"
# b = "hello world"


# print(a is b)

# a = [1, 2, 3]
# b = a
# a += [4]
# a = [1, 2, 3]
# b = a
# a = a + [4]

# print(a)
# print(b)
