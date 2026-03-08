# kortej = (1, 2)
# a, b = kortej
# a = 100
# # kortej = (a, b + 5)
# print(kortej)
# print(a)
# print(b)

# print(2 * 2 * 2 * 2**2)

cash = 287

hundres = cash // 100
rest_of = cash % 100
cash = cash - (hundres * 100)

fifty = rest_of // 50
rest_of = rest_of % 50
cash = cash - (fifty * 50)

twenty = rest_of // 20
rest_of = rest_of % 20
cash = cash - (twenty * 20)

ten = rest_of // 10
rest_of = rest_of % 10
cash = cash - (ten * 10)

five = rest_of // 5
rest_of = rest_of % 5
cash = cash - (five * 5)

one = rest_of // 1
rest_of = rest_of % 1
cash = cash - (one * 1)

print(hundres, fifty, twenty, ten, five, one)
