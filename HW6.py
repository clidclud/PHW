# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума).
# На вход подается список с элементами list_1 и границы диапазона 
# в виде чисел min_number, max_number.
# Пример
# На входе:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# На выходе:


# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19

# from random import randint

# list_1 = []
# len = randint(5,10)
# for _ in range(len):
#     list_1.append(randint(-10, 10))
# print(list_1)

# min_number = int(input("Введите минимальное значение: "))
# max_number = int(input("Введите максимальное значение: "))

# index = 0
# for i in list_1:
#     if i > min_number and i < max_number:
#         print(i, index)
#     index += 1

# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент a1 , разность d и количество элементов n 
# будет задано автоматически. Формула для получения n-го члена 
# прогрессии: an = a1 + (n-1) * d.
# Пример
# На входе:
# a1 = 2
# d = 3
# n = 4
# На выходе:
# 2
# 5
# 8
# 11

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите кол-во элементов: "))

an = a1
for i in range(n):
    print(an)
    an = an + d
    