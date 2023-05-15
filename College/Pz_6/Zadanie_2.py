# Дан целочисленный список размера N, все эелементы которого упорядочены(по возрастанию или убыванию).
# Найти количество различных эелементов в данном списке.

import random
N = int(input("введите размер списка A: "))
spisok = []
res = 0

while res < N:
    spisok.append((float(random.randint(0, 100))))
    res += 1
spisok.sort()
print(spisok)

b = 0
for i in range(len(spisok)):
    if not spisok[i] in spisok[0:i]:
        b += 1
print(b)