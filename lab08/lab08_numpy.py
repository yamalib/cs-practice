import numpy as np

# Задание 1. Создание векторов и матриц

# 1. hours — числа от 0 до 21 с шагом 3
hours = np.arange(0, 22, 3)
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

# 2. line — пять равноудалённых чисел от 0 до 1 включительно
line = np.linspace(0, 1, 5)
print("\nline:", line)

# 3. zeros — вектор из шести нулей целого типа
zeros = np.zeros(6, dtype=int)
print("\nzeros:", zeros)

# 4. unknown_table — матрица формы (2, 3), заполненная -1
unknown_table = np.full((2, 3), -1)
print("\nunknown_table:\n", unknown_table)

# 5. identity — единичная матрица 3×3
identity = np.eye(3)
print("\nidentity:\n", identity)

print()
# Задание 2. Индексы и срезы в векторе

print("hours:", hours)
print("Третий элемент (индекс 2):", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])

print()
# Задание 3. Строки и столбцы таблицы

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("temperatures:\n", temperatures)
print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("Значение из второй строки и третьего столбца (temperatures[1, 2]):", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2×2:\n", temperatures[0:2, 1:3])

print()
# Задание 4. Прямоугольные срезы

matrix = np.arange(1, 26).reshape(5, 5)
print("matrix:\n", matrix)

first_three = matrix[:3]
print("\nПервые три строки:\n", first_three, "\nshape:", first_three.shape)

last_two = matrix[-2:]
print("\nПоследние две строки:\n", last_two, "\nshape:", last_two.shape)

first_two_cols = matrix[:, :2]
print("\nПервые два столбца:\n", first_two_cols, "\nshape:", first_two_cols.shape)

fragment = matrix[1:4, 2:5]
print("\nФрагмент строки 1–3, столбцы 2–4:\n", fragment, "\nshape:", fragment.shape)

corner = matrix[-2:, -2:]
print("\nУгловой блок 2×2 в правом нижнем углу:\n", corner, "\nshape:", corner.shape)

print()
# Задание 5. Изменение массива с помощью срезов

# Примеры
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector после изменения:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix после изменения:\n", small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("\nchanged_hours:", changed_hours)
print("исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0          # всю вторую строку на нули
changed_matrix[:, -1] = -1        # последний столбец на -1
changed_matrix[1:4, 1:4] = 100    # центральный блок 3×3 на 100
print("\nchanged_matrix:\n", changed_matrix)
print("\nисходная matrix:\n", matrix)

print()
print("Задание 6. Изменение формы")

numbers = np.arange(12)
print("numbers:", numbers)
print("shape numbers:", numbers.shape)

table = numbers.reshape(3, 4)
print("\ntable:\n", table)
print("shape table:", table.shape)

transposed = table.T
print("\ntransposed:\n", transposed)
print("shape transposed:", transposed.shape)

