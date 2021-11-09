# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно
# в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_2 = []
print(array_1)

for i in range(len(array_1)):
    if array_1[i] % 2 == 0:
        array_2.append(i)
print(array_2)
