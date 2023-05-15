# Дано трехзначное число. Вывести вначале его последнюю цифру (единицы), а затем — его среднюю цифру (десятки).
try:
    Number = int(input("Введите трехзначное число: "))

    sotni = int(Number / 100)
    print("Сотни - ", sotni)

    tens = int((Number - sotni * 100) / 10)
    print("Десятки - ", tens)

    unit = int(Number % 10)
    print("Единицы - ", unit)

    A = str(unit) + str(tens)
    print("Полученное число - ", A)

except ValueError:
    print("Это не подходящее число")
