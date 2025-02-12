import numpy as np

y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

condition = (y > 3) & (y < 9)

count = np.sum(condition)
print("Количество элементов > 3 и < 9:", count)
