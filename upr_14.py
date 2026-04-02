month = (
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
)

week_days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
first = "Wednesday"  # День недели первого числа.


while True:
    index = 0
    index2 = 0
    while index < len(week_days):
        print(f"{week_days[index][0].rjust(3, " ")}", end="")
        index += 1
    index += 1
    print()

    print(" " * week_days.index(first) * 3, end="")

    while index2 < len(month):
        print(f"{month[index2]:3.0f}", end="")
        index2 += 1
        if (index2 + week_days.index(first)) % 7 == 0:
            print()

    break
