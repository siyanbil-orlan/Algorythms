# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = max_ = 0
for i in range(len(array)):
    if array[i] > array[max_]:
        max_ = i
    elif array[i] < array[min_]:
        min_ = i
array[max_], array[min_] = array[min_], array[max_]
print(array)
