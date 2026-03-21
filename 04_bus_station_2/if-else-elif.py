# value = float(input("Value: "))
# part = float(input("How many part?: "))

# if value <= 0 or part <= 0:
#     print("Negative VALUE, PART or ZIRO values ​​cannot be entered!")
#     x = 2
# else:
#     percent = round(part / value * 100, 2)
#     print(percent, "%")


age = 12

if age < 0 or age > 149:
    print("the is no such a number: " + str(age))
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
else:
    print("Adult")

if 0 <= age <= 12:
    result = "Ребенок"
elif 13 <= age <= 17:
    result = "Подросток"
elif 18 <= age <= 149:
    result = "Взрослый"
else:
    result = f"Возраст не может быть: {age}"

print(result)
