import numpy as np


def make_identity(matrix): # приводим матрицу к еденичному виду
    for nrow in range(len(matrix) - 1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor * row
    return matrix


def gaussPivotFunc(matrix):
    for nrow in range(len(matrix)):
        # nrow равен номеру строки
        # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
        # которая начинается со строки nrow. Поэтому нужно прибавить nrow к результату
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            # swap
            matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
        row = matrix[nrow]
        divider = row[nrow]  # диагональный элемент
        if abs(divider) < 1e-10:#проверка нуля на диагонали
            raise ValueError(
                f"Матрица несовместна. Максимальный элемент в столбце {nrow}: {divider:.3g}"
            )
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[nrow + 1:]:
            factor = lower_row[nrow]  # элемент строки в колонке nrow
            lower_row -= factor * row  # вычитаем, чтобы получить ноль в колонке nrow
    # приводим к диагональному виду
    make_identity(matrix)
    return matrix


m = np.array([2.4,0.2,-0.3,-1.1,5.8,23.84,0.3,0.1,1.1,10.2,1.,38.85,0.5,-6.2,0.1,1.5,-1.2,17.23,0.1,2.1,5.1,0.2,-0.3,6.56,2.5,0.1,0.2,0.3,0.4,6.63])
m = m.reshape((5,6))
print("начальная матрица:")
print(m)

print("\nОтвет:")
for i,x in enumerate(gaussPivotFunc(m)):
    print(f"x{i+1} = {x[-1]}")