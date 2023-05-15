# Дан список A размера N. Вывести его элементы в следующем порядке: A1, An, A2, An-1, A3, An-2...

import random

N = int(input("Введите размера списка A: "))
A = []
res = 0
while res < N:
    A.append((float(random.randint(0, 100))))
    res += 1
print(A)

b = 1
for i in range(int(N / 2)):
    print(A[i])
    print(A[N-b])
    b += 1
