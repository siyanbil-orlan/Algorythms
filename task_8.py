# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу

def output(matrix_):
    for row in matrix_:
        for el in row:
            print(el, end=' ')
        print()


n = 5
m = 4
matrix = [[int(input('Введите число: ')) for el in range(m - 1)] for row in range(n)]

# сразу в одном цикле сделать заполнение и подсчет суммы не получилось, подзабыл как в python с матрицами работать
for row in matrix:
    sum_ = 0
    for el in row:
        sum_ += el
    row.append(sum_)

output(matrix)
