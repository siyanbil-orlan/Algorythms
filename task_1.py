# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

import hashlib


def count_str(some_string):
    full_str = hashlib.sha1(some_string.encode('utf-8')).hexdigest()
    empty_str = hashlib.sha1(''.encode('utf-8')).hexdigest()
    h_lst = []
    for i in range(len(some_string)):
        for j in range(i + 1, len(some_string) + 1):
            hash_ = hashlib.sha1(some_string[i:j].encode('utf-8')).hexdigest()
            if hash_ == full_str or hash_ == empty_str:
                continue
            else:
                if hash_ not in h_lst:
                    h_lst.append(hash_)
    return len(h_lst)


text = input('Введите строку: ')
print(count_str(text))
