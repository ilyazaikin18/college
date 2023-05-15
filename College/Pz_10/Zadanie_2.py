# Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы нижнего регистра на верхний.

res = 0
for i in open('text18-15.txt', encoding='UTF-8'):
    print(i, end='')
    for a in i:
        l = a.islower()
        if l:
            res += 1
print("\nКоличество букв в нижнем регистре : ", res)

f1 = open("text3.txt", 'w', encoding='UTF-8')
for i in open('text18-15.txt', encoding='UTF-8'):
    for j in i:
        if j.islower():
            j = j.upper()
            f1.write(j)
        else:
            f1.write(j)
f1.close()
