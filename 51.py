# url = "http://www.google.com"

# item = url[0]

# print(item)
phone_number = "1800-000-00-00"  # другой номер не писать сюда

# if phone_number.startswith("+"):
#     pass
# else:
#     phone_number = "+" + phone_number

# if not "+" in phone_number:
#     phone_number = "+" + phone_number
# char = phone_number[0]

# if char != "+":
#     phone_number = "+" + phone_number


phone_number = phone_number if phone_number.startswith("+") else "+" + phone_number


print(phone_number)  # "+1800-000-00-00" должно быть так
