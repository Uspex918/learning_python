while True:
    text = input("Введите текст (q для выхода): ")

    if text == "q":
        break

    index = 0
    count = 0

    # считаем пробелы
    while index < len(text):
        if text[index] == " ":
            count += 1
        index += 1

    # количество слов = пробелы + 1
    print("Количество слов:", count + 1)
