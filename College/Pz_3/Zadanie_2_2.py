import random

x = int(random.randrange(-100, 100))
print("Значение x = ", x)


y = int(random.randrange(-100, 100))
print("Значение y = ", y)


if x == 0 and y == 0:
    print("0")
elif x != 0 and y == 0:
    print("1")
elif x == 0 and y != 0:
    print("2")
else:
    print("3")