# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(data):

    def merge_both_parts(arr, left, right):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    if len(data) > 1:
        mid = len(data) // 2
        # не смог придумать вариант без срезов, чтобы можно было обращаться по индексам как в С
        left_part = data[:mid]
        right_part = data[mid:]

        merge_sort(left_part)
        merge_sort(right_part)
        merge_both_parts(data, left_part, right_part)


size = 10
min_item = 0
max_item = 50
array = [random.randint(min_item, max_item - 1) for _ in range(size)]

print(array)
merge_sort(array)
print(array)
