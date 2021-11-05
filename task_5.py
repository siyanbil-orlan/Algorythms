# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

sym = 32
last_sym = 127
in_line = 10
flag = 1  # по-дурацки через флаг, лучше не смог придумать, простите
while flag:
    for i in range(in_line):
        if i < in_line - 1:
            print(f'{sym} - {chr(sym)}', end=', ')
        else:
            print(f'{sym} - {chr(sym)}')
        sym += 1
        if sym > last_sym:
            flag = 0
            break
