# Дан список размера N. Осуществить циклический сдвиг элементов списка влево на одну позицию.
# При этом An перейдет в An-1, An-1 в An-2, ..., A1 в An

import random

N = int(input("Введите размера списка A: "))
spisok = []
res = 0

while res < N:
    spisok.append((float(random.randint(0, 100))))
    res += 1
print(spisok)

def left(massive, shift=1):
    for i in range(shift):
        massive.insert(9, massive.pop(0))
    return massive
print(left(spisok))






