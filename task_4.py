# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

result = tmp = 0
for i in array:
    cnt = 0
    for j in array:
        if j == i:
            cnt += 1
    if cnt > tmp:
        result = i
        tmp = cnt
print(f'{result = }')
