# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# import random

# heads = 0
# tails = 0
# count = input("Введите количество монет на столе: ")
# while not count.isdigit():
#     count = input("Неккоректное число, попробуйте еще раз: ")
# count = int(count)
# for i in range(count):
#     coin = random.randint(0,1)
#     print(coin)
#     if coin == 0: heads += 1
#     if coin == 1: tails += 1
# print("Орлов:", heads, "Решек:", tails)
# if heads > tails: print(tails)
# elif heads < tails: print(heads)
# else: print("Одинаковое количество орлов и решек:", heads)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = input("Введите число S: ")
while not s.isdigit():
    s = input("Неккоректное число, попробуйте еще раз: ")
s = int(s)

p = input("Введите число P: ")
while not p.isdigit():
    p = input("Неккоректное число, попробуйте еще раз: ")
p = int(p)
print("Сумма чисел:",s,"Произведение чисел:",p)

y = s

for x in range(1, s // 2 + 1):
    y -= 1
    if x * y == p: print(x, "+", y, "=", s, "||", x, "*", y, "=", p)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = input("Введите число N: ")
# while not n.isdigit():
#     n = input("Неккоректное число, попробуйте еще раз: ")
# n = int(n)

# i = 1
# while i < n:
#     print(i)
#     i *= 2