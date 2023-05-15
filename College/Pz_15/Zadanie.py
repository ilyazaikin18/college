# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные суммы.
# В матрице найти минимальный элемент в предпоследней строке.

import random

rows, columns = 4, 4

matrix = ([[random.randrange(5, 10) for x in range(rows)] for y in range(columns)])
print('Начальная матрица: ')
for i in matrix:
    print(i)

# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
matrix_sum = []
for i in range(len(matrix[0])):
    stowbtsy = 0
    for j in range(len(matrix)):
        stowbtsy += matrix[j][i]
    matrix_sum.append(stowbtsy)
print('Сумма элементов всех столбцов: ')
print(matrix_sum, '\n')

# Выполнить замену элементов второй строки исходной матрицы на полученные суммы.
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == rows - 3:
            matrix[i][j] = matrix_sum[j]
print('Замена второй строки на полученные элементы: ')
for i in matrix:
    print(i)

# В матрице найти минимальный элемент в предпоследней строке.
print('Минимальный элемент в предпоследней строке: ', min(matrix[columns - 2]))
