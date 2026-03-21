# x = "AAA"
# y = x
# z = "AAA"

# print(id(x))
# print(id(y))
# print(id(z))

# x = x + "a"
# z = z + "c"

# print(id(x))
# print(id(y))
# print(id(z))
# print(x)
# print(y)
# print(z)


# x = "AAA"
# y = x
# z = "AAA"
# print(x is y is z)

# y = input()
# del y
# print(y)


# import sys


# # print(sys.path)
# print(sys.platform)
# print(sys.getrecursionlimit())
# print(sys.argv)


# import sys

# name = sys.argv[1]
# age = sys.argv[2]

# print("Имя:", name)
# print("Возраст:", int(age) + 1)

# import sys

# y = input()
# x = y
# print(sys.getrefcount(y))


# a = 5
# b = a
# b = 10

# print(a)
# print(b)

import sys

x = 5
y = int(input())

print(sys.getrefcount(x))
print(sys.getrefcount(y))
print(id(x))
print(id(y))
