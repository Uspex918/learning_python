gmail_user_email = (
    "nobodyknowsmyage92@gmail.com"  # выдуманный адрес почты который создал юзер
)


# Нужно создать для него автоматически почты на других потовых серверах.
# У почтовых серверов домены это то что после символа @.

# Извлеките при помощи индексов и срезов из gmail_user_email
# почту пользователя "nobodyknowsmyage92" (индекс определите через
# метод строк index). И создайте для него почты на таких серверах:

outlook_domain = "@outlook.com"
proton_mail_domain = "@proton.me"

# ВАШ КОД ТУТ
stop = gmail_user_email.index("@")
user = gmail_user_email[:stop]
outlook_user_email = user + outlook_domain
proton_user_email = user + proton_mail_domain

# результат должен быть в этих переменных:
print(outlook_user_email)  # nobodyknowsmyage92@outlook.com
print(proton_user_email)  # nobodyknowsmyage92@proton.me
