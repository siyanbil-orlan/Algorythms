# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры

def count_sum(n):
    if n == 1:
        return 1
    return -(count_sum(n - 1)) / 2 + 1


n = int(input('Введите количество элементов: '))
result = count_sum(n)
print(f'sum = {result}')
