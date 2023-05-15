# В последовательности на n целых чисел найти и вывести:
# 1.максимальный среди положительных
# 2.минимальный среди отрицательных
# 3.произведение элементов

import random
n = int(input('Количество случайных символов: '))

a = [random.randint(-20, 30) for x in range(n)]
b = [n for n in a if n > 0]
c = [n for n in a if n < 0]

answer = 1
for i in a:
    answer *= i

max_number = max(b)
min_number = min(c)

print(a)
print(b)
print(c)
print("Максимальный среди положительных", max_number)
print("Минимальный среди отрицательных", min_number)
print("Произведение элементов", answer)