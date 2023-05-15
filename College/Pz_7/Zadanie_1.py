# Дана строка. Подсчитать общее количество содержащихся в ней строчных латинских и русских букв.

alfavit = ("абвгдеёжзиЙклмнопрстуфчцчшщъьэюabcdefghijklmnopqrstuvwxyz")
s1 = ("There is my house. - Это мой дом.")
res = 0

for i in s1:
    if i in alfavit:
        res += 1
print(res)
