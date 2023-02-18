for i in range(99999):
    number = int(input("Введите номер вагона: "))
    if number >= 1 and number <= 36 and number % 2 == 0:
        print("Ваше место в купе наверху")
        break
    elif number >= 1 and number <= 36 and number % 2 == 1:
        print("Ваше место в купе снизу")
        break
    elif number > 36 and number <= 54 and number % 2 == 0:
        print("Ваше место сбоку наверху")
        break
    elif number > 36 and number <= 54 and number % 2 == 1:
        print("Ваше место сбоку снизу")
        break
    else:
        print("Введите правильное место (от 1 до 54 включительно)")
