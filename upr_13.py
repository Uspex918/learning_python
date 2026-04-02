currencies = ("USD", "EUR", "GBP", "JPY", "CNY")
rates = (93, 101, 115, 0.63, 12.8)


index = 0
while index < len(currencies):
    print(f"{currencies[index]} | {rates[index]:6.2f}")
    # print(f"{currencies[index]} | {str(rates[index]).rjust(4, " ")}")
    index += 1
