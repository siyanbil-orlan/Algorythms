# Для данного задания была взята задача №6 урока №3, которую мною использовалась в четвертом практическом задании.
# Python 3.7.4
# OS x64
# Не понял как считать размер памяти для i в цикле. Это один объект постоянного размера, который имеет адрес на элемент
# итерируемого объекта? И что делать с range? Вызов данной функции создает список, который так же использует оперативную
# память?

import random
import sys


def main(array):
    min_ = max_ = 0
    for i in range(len(array)):
        if array[i] > array[max_]:
            max_ = i
    for j in range(len(array)):
        if array[j] < array[min_]:
            min_ = j

    if max_ > min_:
        max_ = max_ ^ min_
        min_ = max_ ^ min_
        max_ = max_ ^ min_

    if min_ - max_ == 1:
        return 'Нет элементов между max и min'
    else:
        result = sum(array[max_+1:min_])

    # добавляем в словарь локальные переменные для вычисления занимаемой памяти
    for key, value in locals().items():
        a.append(value)

    return result


def main_2(arr):
    min_ = max_ = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_]:
            max_ = i
        elif arr[i] < arr[min_]:
            min_ = i
    if max_ > min_:
        max_, min_ = min_, max_
    if min_ - max_ == 1:
        return 'Нет элементов между max и min'
    else:
        result = 0
        for j in arr[max_ + 1:min_]:
            result += j

    # добавляем в словарь локальные переменные для вычисления занимаемой памяти
    for key, value in locals().items():
        a.append(value)

    return result


def main_3(arr):
    min_ = max_ = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_]:
            max_ = i
        elif arr[i] < arr[min_]:
            min_ = i

    if max_ > min_:
        max_ = max_ ^ min_
        min_ = max_ ^ min_
        max_ = max_ ^ min_

    if min_ - max_ == 1:
        return 'Нет элементов между max и min'
    else:
        result = sum(arr[max_ + 1:min_])

    # добавляем в словарь локальные переменные для вычисления занимаемой памяти
    for key, value in locals().items():
        a.append(value)

    return result


def my_getsize(obj):
    if hasattr(obj, '__iter__'):
        res = 0
        for el in obj:
            res += my_getsize(el)
        res += sys.getsizeof(obj)
        return res
    return sys.getsizeof(obj)


size = 100
min_item = 0
max_item = 100
array_ = [random.randint(min_item, max_item) for _ in range(size)]

a = []
main(array_)
print(f'Функция main, принимающая список длинной {size} элементов, занимает {my_getsize(a)} байт')

a = []
main_2(array_)
print(f'Функция main_2, принимающая список длинной {size} элементов, занимает {my_getsize(a)} байт')

a = []
main_3(array_)
print(f'Функция main_3, принимающая список длинной {size} элементов, занимает {my_getsize(a)} байт')

# Вывод:
# Последние темы даются с трудом. Как выполнить второе задание пятого урока так и не разобрался.
# Написать универсальную функцию, которая принимала бы другую функцию и возвращала объем используемой ей памяти,
# не вышло. Первые две функции используют больше памяти из-за двух циклов в теле. В целом следует использовать меньше
# переменных и циклов.
