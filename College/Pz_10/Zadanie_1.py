# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:

list1 = ['99 6 12 36 20 45 100 15']
f1 = open('text1.txt', 'w', encoding='UTF-8')
f1.writelines(list1)
f1.close()

f1 = open('text1.txt', encoding='UTF-8')
row1 = f1.read()
arr1 = row1.split()
for i in range(len(arr1)):
 arr1[i] = int(arr1[i])
f1.close()

f1 = open('text1.txt', 'w', encoding='UTF-8')
d, t = 0, 0
for i in range(len(arr1)):
 d = min(arr1)
for i in range(len(arr1)):
 if arr1[i] == d:
  t = i
  break
f1.write("\n")
f1.close()

f1 = open('text1.txt', 'w', encoding='UTF-8')
list2 = [99, 6, 12, 36, 20, 45, 100, 15]
firstlen = list2[0]
for i in range(len(list2)):
 list2[i] *= firstlen
f1.close()

l = ""
for i in list2:
 l += str(i) + " "

f1 = open('text1.txt', 'w', encoding='UTF-8')
f1.write('Содержимое первого файла:  ')
f1.writelines(list1)
f1.write('\n')
f1.close()

f2 = open('text2.txt', 'w', encoding='UTF-8')
f2.write('Исходные данные:  ')
f2.writelines(list1)
f2.write('\n')

f2.write('Количество элементов:  ')
f2.writelines(str(len(arr1)))
f2.write('\n')

f2.write('Индекс последнего минимального элемента:  ')
f2.writelines(str(t))
f2.write('\n')

f2.write('Умноженные элементы: ')
f2.write(str(l))
f2.write('\n')



