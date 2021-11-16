import math
import timeit
import cProfile


def sieve(n):
    a = [2]
    cnt = 0
    m = a[0] + 1
    while cnt < n-1:
        flag = 1
        for el in a:
            if m % el == 0:
                flag = 0
                break
        if flag == 1:
            a.append(m)
            cnt += 1
        m += 1
    return a[-1]


print(timeit.timeit('sieve(4)', number=1000, globals=globals()))     # 0.004721283999999992
print(timeit.timeit('sieve(8)', number=1000, globals=globals()))     # 0.010921498000000002
print(timeit.timeit('sieve(16)', number=1000, globals=globals()))    # 0.037774380999999996
print(timeit.timeit('sieve(32)', number=1000, globals=globals()))    # 0.107972067
print(timeit.timeit('sieve(64)', number=1000, globals=globals()))    # 0.340747328
print(timeit.timeit('sieve(128)', number=1000, globals=globals()))   # 1.1668413340000001
print(timeit.timeit('sieve(256)', number=1000, globals=globals()))   # 4.147807319
print(timeit.timeit('sieve(512)', number=1000, globals=globals()))   # 16.477010406999998
print(timeit.timeit('sieve(1024)', number=1000, globals=globals()))  # 66.551013681
print(timeit.timeit('sieve(2048)', number=1000, globals=globals()))  # 263.44752606299994

cProfile.run('sieve(1000)')
#          1003 function calls in 0.082 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.082    0.082 <string>:1(<module>)
#         1    0.082    0.082    0.082    0.082 task_2.py:6(sieve)
#         1    0.000    0.000    0.082    0.082 {built-in method builtins.exec}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve(10000)')
#          10003 function calls in 6.391 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    6.391    6.391 <string>:1(<module>)
#         1    6.388    6.388    6.390    6.390 task_2.py:6(sieve)
#         1    0.000    0.000    6.391    6.391 {built-in method builtins.exec}
#      9999    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def prime(n):
    cnt = 0
    i = 2

    def is_prime(num):
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                return False
        return True

    while True:
        if is_prime(i) is True:
            cnt += 1
        if cnt == n:
            break
        i += 1
    return i


print(timeit.timeit('prime(4)', number=1000, globals=globals()))     # 0.006828010000000009
print(timeit.timeit('prime(8)', number=1000, globals=globals()))     # 0.020685294999999992
print(timeit.timeit('prime(16)', number=1000, globals=globals()))    # 0.07233066199999999
print(timeit.timeit('prime(32)', number=1000, globals=globals()))    # 0.373917014
print(timeit.timeit('prime(64)', number=1000, globals=globals()))    # 0.6282701029999999
print(timeit.timeit('prime(128)', number=1000, globals=globals()))   # 1.165215092
print(timeit.timeit('prime(256)', number=1000, globals=globals()))   # 2.796427438
print(timeit.timeit('prime(512)', number=1000, globals=globals()))   # 7.177251982
print(timeit.timeit('prime(1024)', number=1000, globals=globals()))  # 18.178927219
print(timeit.timeit('prime(2048)', number=1000, globals=globals()))  # 46.333960919000006

cProfile.run('prime(1000)')
#          15840 function calls in 0.024 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#         1    0.004    0.004    0.024    0.024 task_2.py:59(prime)
#      7918    0.018    0.000    0.020    0.000 task_2.py:63(is_prime)
#         1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#      7918    0.001    0.000    0.001    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(10000)')
#          209460 function calls in 0.529 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.529    0.529 <string>:1(<module>)
#         1    0.057    0.057    0.529    0.529 task_2.py:47(prime)
#    104728    0.453    0.000    0.473    0.000 task_2.py:51(is_prime)
#         1    0.000    0.000    0.529    0.529 {built-in method builtins.exec}
#    104728    0.020    0.000    0.020    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime(100000)')
#          2599420 function calls in 14.713 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   14.713   14.713 <string>:1(<module>)
#         1    0.692    0.692   14.713   14.713 task_2.py:47(prime)
#   1299708   13.765    0.000   14.020    0.000 task_2.py:51(is_prime)
#         1    0.000    0.000   14.713   14.713 {built-in method builtins.exec}
#   1299708    0.255    0.000    0.255    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

n = int(input("Введите номер простого числа: "))
print(f'Простое число с порядковым номером "{n}" = {prime(n)}')
print(f'Простое число с порядковым номером "{n}" = {sieve(n)}')

# Оба алгоритма имеют линейную асимптотику O(n). Первая функция показала чуть более лучшие результаты при n < 128,
# при n > 128 вторая функция работает заметно быстрее (судя по всему за счет перебора чисел до квадратного корня от n,
# что значительно уменьшает время работы алгоритма). Оптимальной из данных двух является фунция prime, однако,
# в дальнейшем следует избавиться от внутренней функции is_prime, что, вероятно, положительно скажется на скорости
# алгоритма.
