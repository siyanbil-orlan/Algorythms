# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

import random


def slice_(arr):
    min_ = max_ = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_]:
            max_ = i
        elif arr[i] < arr[min_]:
            min_ = i
    if max_ > min_:
        max_, min_ = min_, max_
    return max_, min_


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if slice_(array)[1] - slice_(array)[0] == 1:
    print('Нет элементов между max и min')
else:
    result = 0
    for i in array[slice_(array)[0]+1:slice_(array)[1]]:
        result += i
    print(f'{result = }')
