# vowels = "aeiouy"

# player1 = input("Имя 1 игрока: ")
# player2 = input("Имя 2 игрока: ")

# score1 = 0
# score2 = 0

# current_player = 1

# while True:
#     if current_player == 1:
#         name = player1
#     else:
#         name = player2

#     word = input(f"{name}, введи слово: ").lower()

#     if word in ["exit", "quit", "q"]:
#         break

#     count = 0
#     for char in word:
#         if char in vowels:
#             count += 1
#     print(f"Гласных: {count}")

#     if current_player == 1:
#         score1 += count
#         current_player = 2
#     else:
#         score2 += count
#         current_player = 1

# print("Игра окончена!")
# print(f"{player1}: {score1}")
# print(f"{player2}: {score2}")

# if score1 > score2:
#     print(f"Победил {player1}")
# elif score2 > score1:
#     print(f"Победил {player2}")
# else:
#     print("Ничья!")

# Новые строки кода помечены #!!!

print("Добро пожаловать в игру в слова!")  #!!!

player1 = input("Имя игрока 1: ")  #!!!
player2 = input("Имя игрока 2: ")  #!!!

player1_scores = 0  #!!!
player2_scores = 0  #!!!

turn = player1  #!!!

while True:  #!!!

    user_input = input(f"{turn}, введите слово (exit для выхода):\n>").lower()

    if user_input == "exit":  #!!!
        break  #!!!

    vowels = "eyuioa"
    vowels_count = 0
    index = 0

    while index < len(user_input):
        char = user_input[index]
        index += 1

        if char in vowels:

            vowels_count += 1

        elif char == "t":
            break

    if turn == player1:  #!!!
        print(f"{player1} - {vowels_count}")  #!!!
        player1_scores += vowels_count  #!!!
        turn = player2  #!!!
    else:  #!!!
        print(f"{player2} - {vowels_count}")  #!!!
        player2_scores += vowels_count  #!!!
        turn = player1  #!!!

print("Results")  #!!!
print(f"{player1} - {player1_scores}\n{player2} - {player2_scores}")
