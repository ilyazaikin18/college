# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».
a = input("Введите целое число a: ")
while type(a) !=int:
    try:
        a = int(a)
    except ValueError:
        print("Целое число а, введено неверно")
        a = input("Введите целое число a: ")


b = input("Введите целое число b: ")
while type(b) !=int:
    try:
        b = int(b)
    except ValueError:
        print("Целое число b, введено неверно")
        b = input("Введите целое число b: ")


c = input("Введите целое число c: ")
while type(c) !=int:
    try:
        c = int(c)
    except ValueError:
        print("Целое число c, введено неверно")
        c = input("Введите целое число b: ")


if (a > 0) and (b < 0) and (c < 0):
    print("Число а положительное")
elif (b > 0) and (a < 0) and (c < 0):
    print("Число b положительное")
elif (c > 0) and (b < 0) and (a < 0):
    print("Число c положительное")
elif (a > 0) and (b > 0) and (c > 0):
    print("Все числа положительные")
elif (a < 0) and (b < 0) and (c < 0):
    print("Все числа отрицательные")
    