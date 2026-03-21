# user_input = "привеТ !"
# ca = user_input.find("ив")
# print(ca)
# word = "привет"

# if word in user_input.casefold():
#     print("Привет")


# user_input = "255,5"

# # if "," in user_input:
# #     user_input = float(user_input.replace(",", "."))

# print(user_input.count("5"))

# b_2_b = "b2b and"

# print(b_2_b.partition(" "))
# print(b_2_b[::2])

user_input = "http://www.google.com"

if user_input.startswith("http://"):
    user_input = user_input.replace("http://", "https://", 1)
print(user_input)
