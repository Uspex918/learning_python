temps = (12, 15, 14, 10, 9, 11, 13)  # кортежи одинаковой длины.
week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

i = 0
while i < len(temps):
    print(f"{week[i]}: {str(temps[i]).rjust(3, " ")} °C")
    # print(f"{week[i]}: {temps[i]:5.1f} °C")
    i += 1
