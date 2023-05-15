# Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму 1 + A + A2 + A3 + ... + AN.
A = input("Введите вещественное число A: ")
while type(A) != float:
    try:
        A = float(A)
    except ValueError:
        print("Неправильно введено число")
        A = input("Введите вещественное число A: ")

N = input("Введите целое число N: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно введено число")
        N = input("Введите целое число N: ")

B = 1
t = 0
n = N
while t < N:
    B += A ** n
    t += 1
    n -= 1
print("Сумма равна : ", B)