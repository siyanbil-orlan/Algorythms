# Для первого задания была взята задача №8 урока №3.
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

import timeit
import cProfile
import random


def main(n):
    size = n
    min_item = 0
    max_item = 100
    array_ = [random.randint(min_item, max_item) for _ in range(size)]

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

    if slice_(array_)[1] - slice_(array_)[0] == 1:
        return 'Нет элементов между max и min'
    else:
        result = 0
        for j in array_[slice_(array_)[0] + 1:slice_(array_)[1]]:
            result += j
    return result


print(timeit.timeit('main(4)', number=1000, globals=globals()))      # 0.019758021000000014
print(timeit.timeit('main(8)', number=1000, globals=globals()))      # 0.029080004999999992
print(timeit.timeit('main(16)', number=1000, globals=globals()))     # 0.05206681200000002
print(timeit.timeit('main(32)', number=1000, globals=globals()))     # 0.10722313899999997
print(timeit.timeit('main(64)', number=1000, globals=globals()))     # 0.19398875
print(timeit.timeit('main(128)', number=1000, globals=globals()))    # 0.39848256400000004
print(timeit.timeit('main(256)', number=1000, globals=globals()))    # 0.8509549930000001
print(timeit.timeit('main(512)', number=1000, globals=globals()))    # 1.597529485
print(timeit.timeit('main(1024)', number=1000, globals=globals()))   # 3.151294506
print(timeit.timeit('main(2048)', number=1000, globals=globals()))   # 6.336662532000001

cProfile.run('main(10000)')
#       52709 function calls in 0.047 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.047    0.047 <string>:1(<module>)
#  10000    0.010    0.000    0.014    0.000 random.py:237(_randbelow_with_getrandbits)
#  10000    0.011    0.000    0.024    0.000 random.py:290(randrange)
#  10000    0.006    0.000    0.030    0.000 random.py:334(randint)
#      1    0.006    0.006    0.036    0.036 task_1.py:10(<listcomp>)
#      4    0.012    0.003    0.012    0.003 task_1.py:12(slice_)
#      1    0.000    0.000    0.047    0.047 task_1.py:6(main)
#      1    0.000    0.000    0.047    0.047 {built-in method builtins.exec}
#      4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12696    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('main(100000)')
#       526941 function calls in 0.700 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.700    0.700 <string>:1(<module>)
# 100000    0.120    0.000    0.170    0.000 random.py:237(_randbelow_with_getrandbits)
# 100000    0.173    0.000    0.343    0.000 random.py:290(randrange)
# 100000    0.072    0.000    0.415    0.000 random.py:334(randint)
#      1    0.168    0.168    0.583    0.583 task_1.py:10(<listcomp>)
#      4    0.116    0.029    0.116    0.029 task_1.py:12(slice_)
#      1    0.000    0.000    0.699    0.699 task_1.py:6(main)
#      1    0.000    0.000    0.700    0.700 {built-in method builtins.exec}
#      4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 100000    0.023    0.000    0.023    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 126928    0.027    0.000    0.027    0.000 {method 'getrandbits' of '_random.Random' objects}


def main_2(n):
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    min_ = max_ = 0
    for i in range(len(array)):
        if array[i] > array[max_]:
            max_ = i
        elif array[i] < array[min_]:
            min_ = i
    if max_ > min_:
        max_, min_ = min_, max_
    if min_ - max_ == 1:
        return 'Нет элементов между max и min'
    else:
        result = 0
        for j in array[max_+1:min_]:
            result += j
    return result


print(timeit.timeit('main_2(4)', number=1000, globals=globals()))      # 0.017166629000000003
print(timeit.timeit('main_2(8)', number=1000, globals=globals()))      # 0.025758849
print(timeit.timeit('main_2(16)', number=1000, globals=globals()))     # 0.055087822999999994
print(timeit.timeit('main_2(32)', number=1000, globals=globals()))     # 0.08190601799999997
print(timeit.timeit('main_2(64)', number=1000, globals=globals()))     # 0.15383031600000002
print(timeit.timeit('main_2(128)', number=1000, globals=globals()))    # 0.29407692900000004
print(timeit.timeit('main_2(256)', number=1000, globals=globals()))    # 0.6092432950000001
print(timeit.timeit('main_2(512)', number=1000, globals=globals()))    # 1.1514156850000001
print(timeit.timeit('main_2(1024)', number=1000, globals=globals()))   # 2.299663057
print(timeit.timeit('main_2(2048)', number=1000, globals=globals()))   # 4.638192276

cProfile.run('main_2(10000)')
#          52851 function calls in 0.040 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.040    0.040 <string>:1(<module>)
#     10000    0.010    0.000    0.014    0.000 random.py:237(_randbelow_with_getrandbits)
#     10000    0.011    0.000    0.025    0.000 random.py:290(randrange)
#     10000    0.006    0.000    0.031    0.000 random.py:334(randint)
#         1    0.003    0.003    0.040    0.040 task_1.py:83(main_2)
#         1    0.006    0.006    0.037    0.037 task_1.py:87(<listcomp>)
#         1    0.000    0.000    0.040    0.040 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12845    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('main_2(100000)')
#          526701 function calls in 0.427 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.426    0.426 <string>:1(<module>)
#    100000    0.105    0.000    0.143    0.000 random.py:237(_randbelow_with_getrandbits)
#    100000    0.115    0.000    0.258    0.000 random.py:290(randrange)
#    100000    0.063    0.000    0.321    0.000 random.py:334(randint)
#         1    0.025    0.025    0.426    0.426 task_1.py:83(main_2)
#         1    0.079    0.079    0.401    0.401 task_1.py:87(<listcomp>)
#         1    0.000    0.000    0.427    0.427 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    100000    0.015    0.000    0.015    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    126695    0.023    0.000    0.023    0.000 {method 'getrandbits' of '_random.Random' objects}


def main_3(n):
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    min_ = max_ = 0
    for i in range(len(array)):
        if array[i] > array[max_]:
            max_ = i
        elif array[i] < array[min_]:
            min_ = i

    if max_ > min_:
        max_ = max_ ^ min_
        min_ = max_ ^ min_
        max_ = max_ ^ min_

    if min_ - max_ == 1:
        return 'Нет элементов между max и min'
    else:
        result = sum(array[max_+1:min_])
    return result


print(timeit.timeit('main_3(4)', number=1000, globals=globals()))      # 0.012287398000000005
print(timeit.timeit('main_3(8)', number=1000, globals=globals()))      # 0.019346656000000004
print(timeit.timeit('main_3(16)', number=1000, globals=globals()))     # 0.03507386400000001
print(timeit.timeit('main_3(32)', number=1000, globals=globals()))     # 0.072706089
print(timeit.timeit('main_3(64)', number=1000, globals=globals()))     # 0.152885057
print(timeit.timeit('main_3(128)', number=1000, globals=globals()))    # 0.271142399
print(timeit.timeit('main_3(256)', number=1000, globals=globals()))    # 0.5614628939999999
print(timeit.timeit('main_3(512)', number=1000, globals=globals()))    # 1.133488986
print(timeit.timeit('main_3(1024)', number=1000, globals=globals()))   # 2.245744978
print(timeit.timeit('main_3(2048)', number=1000, globals=globals()))   # 4.408090122

cProfile.run('main_3(10000)')
#       52598 function calls in 0.046 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.046    0.046 <string>:1(<module>)
#  10000    0.011    0.000    0.015    0.000 random.py:237(_randbelow_with_getrandbits)
#  10000    0.014    0.000    0.029    0.000 random.py:290(randrange)
#  10000    0.006    0.000    0.035    0.000 random.py:334(randint)
#      1    0.003    0.003    0.046    0.046 task_1.py:154(main_3)
#      1    0.009    0.009    0.043    0.043 task_1.py:158(<listcomp>)
#      1    0.000    0.000    0.046    0.046 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#  10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12591    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('main_3(100000)')
#       526753 function calls in 0.445 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.445    0.445 <string>:1(<module>)
# 100000    0.095    0.000    0.133    0.000 random.py:237(_randbelow_with_getrandbits)
# 100000    0.117    0.000    0.249    0.000 random.py:290(randrange)
# 100000    0.100    0.000    0.349    0.000 random.py:334(randint)
#      1    0.028    0.028    0.444    0.444 task_1.py:154(main_3)
#      1    0.067    0.067    0.416    0.416 task_1.py:158(<listcomp>)
#      1    0.000    0.000    0.445    0.445 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
# 100000    0.017    0.000    0.017    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 126746    0.021    0.000    0.021    0.000 {method 'getrandbits' of '_random.Random' objects}


def main_4(n):
    size = n
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]

    min_ = max_ = 0
    for i in range(len(array)):
        if array[i] > array[max_]:
            max_ = i
    for i in range(len(array)):
        if array[i] < array[min_]:
            min_ = i

    if max_ > min_:
        max_ = max_ ^ min_
        min_ = max_ ^ min_
        max_ = max_ ^ min_

    if min_ - max_ == 1:
        return 'Нет элементов между max и min'
    else:
        result = sum(array[max_+1:min_])
    return result


print(timeit.timeit('main_4(4)', number=1000, globals=globals()))      # 0.012287398000000005
print(timeit.timeit('main_4(8)', number=1000, globals=globals()))      # 0.019346656000000004
print(timeit.timeit('main_4(16)', number=1000, globals=globals()))     # 0.03507386400000001
print(timeit.timeit('main_4(32)', number=1000, globals=globals()))     # 0.072706089
print(timeit.timeit('main_4(64)', number=1000, globals=globals()))     # 0.152885057
print(timeit.timeit('main_4(128)', number=1000, globals=globals()))    # 0.271142399
print(timeit.timeit('main_4(256)', number=1000, globals=globals()))    # 0.5614628939999999
print(timeit.timeit('main_4(512)', number=1000, globals=globals()))    # 1.133488986
print(timeit.timeit('main_4(1024)', number=1000, globals=globals()))   # 2.245744978
print(timeit.timeit('main_4(2048)', number=1000, globals=globals()))   # 4.408090122

cProfile.run('main_3(10000)')
#          52608 function calls in 0.044 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.044    0.044 <string>:1(<module>)
#     10000    0.010    0.000    0.014    0.000 random.py:237(_randbelow_with_getrandbits)
#     10000    0.014    0.000    0.029    0.000 random.py:290(randrange)
#     10000    0.006    0.000    0.034    0.000 random.py:334(randint)
#         1    0.003    0.003    0.044    0.044 task_1.py:158(main_3)
#         1    0.007    0.007    0.041    0.041 task_1.py:162(<listcomp>)
#         1    0.000    0.000    0.044    0.044 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#     10000    0.002    0.000    0.002    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12601    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('main_3(100000)')
#          526913 function calls in 0.453 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.453    0.453 <string>:1(<module>)
#    100000    0.120    0.000    0.158    0.000 random.py:237(_randbelow_with_getrandbits)
#    100000    0.120    0.000    0.278    0.000 random.py:290(randrange)
#    100000    0.086    0.000    0.364    0.000 random.py:334(randint)
#         1    0.029    0.029    0.453    0.453 task_1.py:158(main_3)
#         1    0.061    0.061    0.424    0.424 task_1.py:162(<listcomp>)
#         1    0.000    0.000    0.453    0.453 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#    100000    0.014    0.000    0.014    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    126906    0.023    0.000    0.023    0.000 {method 'getrandbits' of '_random.Random' objects}

# Вывод:
# Все алгоритмы имеют линейную асимптотику O(n). Первый вариант, выполненный в рамках практического задания является
# наихудшим из-за четырехкратного вызова внетренней функции slice_. Во втором варианте я, как вы и советовали, избавился
# от функции slice_, просто используя переменные для хранения значений max и min, что позволило сократить время
# выполнения алгоритма. В третьем варианте используется встроенная функция sum() и битовое исключающее ИЛИ для обмена
# значений переменных. Вариант три немного быстрее второго. В четвертом варианте попытка ухудшить алгоритм путем
# нахождения max и min в двух циклах не принесла ожидаемого результата - алгоритм три тех же n работает с сопоставимой
# скоростью. Оптимальным вариантом считаю алгоритм №3.
