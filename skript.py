#!/usr/bin/python3
import math

# Задание 1.

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
print("a + b:", a + b, "\na - b:", a - b, "\na * b:", a * b, "\na / b:", a / b, "\na % b:", a % b)
print(" a**b:", a**b, "\n a//b:", a//b)

# Задание 2.

print("Здравствуйте,", input("Введите ваше имя: "))

# Задание 3.

print("Последние два символа в обратном порядке:", input("Введите строку: ")[:-3:-1])

# Задание 4.

r = float(input("Введите радиус окружности: "))
if r >= 0:
    print("Площадь окружности:", math.pi * r**2)
else:
    print("Неверный формат")
