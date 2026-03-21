x = 255
y = 255.0

new_obj = y.is_integer()

print(new_obj)


if y.is_integer():
    y = int(y)
else:
    y = round(y)

print(y)
