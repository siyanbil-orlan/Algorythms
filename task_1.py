# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random


def bubble_sort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


size = 10
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item - 1) for _ in range(size)]

print(array)
bubble_sort(array)
print(array)
