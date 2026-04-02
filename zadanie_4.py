# word = "python"
# secret = "_" * len(word)

# while True:
#     print(secret)

#     letter = input("Enter the letter: ").strip().lower()

#     if letter in ["exit", "quit", "q"]:
#         print("Выход из игры")
#         break

#     new_secret = ""
#     index = 0

#     while index < len(word):
#         if word[index] == letter:
#             new_secret += letter
#         else:
#             new_secret += secret[index]

#         index += 1
#     secret = new_secret

#     if secret == word:
#         print(secret)
#         print("Ты угадал слово 🎉")
#         break

# word = "python"
# secret = "_" * len(word)

# while True:
#     letter = input("Enter letter: ").strip().lower()

#     if letter == word:  # Если угадал полное слово. То есть,
#         print("You WIN!")  # просто сразу его целиком ввел.
#         break  # прерываем цикл и всё программу соответственно.

#     if len(letter) != 1:  # если ввел не одну букву (пустой ввод или 2, 3 буквы)
#         print("Вводить только 1 букву за раз!")
#         continue  # идем на круг заново

#     new_secret = ""  # Формируем новый secret
#     index = 0
#     while index < len(secret):
#         char = word[index]
#         if letter == char:
#             # Если буква встретилась добавляем к new_secret
#             new_secret += letter
#         else:
#             # Если буква НЕ встретилась добавляем к new_secret
#             # то что было в "старом" secret под этим индексом.
#             new_secret += secret[index]
#         index += 1
#     secret = new_secret

#     print(f"Word - {secret}")
#     if secret == word:  # А это уже если "побуквенно" слово угадалось.
#         print("You WIN!")
#         break


word = "python"
secret = "_" * len(word)
run = True

while run:
    user_input = str(input("Enter a letter: "))
    if user_input in word:
        index = 0
        while index <= len(word) - 1:
            if word[index] == user_input:
                secret = secret[:index:] + user_input + secret[index + 1 : :]
                print(secret)
                if secret == word:
                    print("You win!!!")
                    run = False
            index += 1
