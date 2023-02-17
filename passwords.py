for i in range(999999999):
    password = input("Введите пароль: ")
    passconfirm = input("Подтвердите пароль: ")
    if len(password) < 7 or (password[0:8] == "qwerty12" or password[0:8] == "12345678"):
        print("Ненадежный пароль. Попробуйте другой пароль!")
    elif password == passconfirm:
        print("Пароль принят!")
        break
    else:
        print("Пароли не совпадают. Попробуйте еще раз!")