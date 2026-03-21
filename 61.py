user_input = input("Enter something:\n")

vowels = "eyuioa"
vowels_count = 0
index = 0

while index < len(user_input):
    if user_input[index] in vowels:
        vowels_count += 1
    elif user_input[index] == "t":
        break
    index += 1

print(vowels_count)
