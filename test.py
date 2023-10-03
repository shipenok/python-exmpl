import numpy as np

# Ваша большая матрица
matrix = np.random.randint(low=-1671, high=1672, size=(100, 100))
print(matrix)
# Создание новой матрицы, в которой значения в соответствии
# с условием замены чисел n на -n и наоборот
new_matrix = np.where(matrix < 0, -matrix, matrix)

# Нахождение разности между исходной матрицей и новой матрицей
difference_matrix = matrix - new_matrix

# Использование разности для получения индексов симметричных переменных
symmetric_indices = np.where(difference_matrix == 0)

# Получение симметричных переменных из исходной матрицы
symmetric_values = matrix[symmetric_indices]

# Вывод множества симметричных переменных
print(set(symmetric_values))