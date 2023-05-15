# Составить генератор (yield), который выводит из строки только буквы.

from string import ascii_letters
def letters(lst):
    yield from [n for n in lst if n in ascii_letters]

a = "I go to college every day except Sunday"
list1 = ""
for i in letters(a):
    list1 += i
print(list1)
