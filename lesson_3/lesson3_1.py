import pandas as pd
import numpy as np

series1 = pd.Series([1, 2, 3], name="A")
series2 = pd.Series([4, 5, 6], name="B")
df_series = pd.DataFrame({'A': series1, 'B': series2})
print("DataFrame из объектов Series:")
print(df_series)

list_dicts = [{'name': 'VLADIMIR', 'age': 72}, {'name': 'Donald', 'age': 78}, {'name': 'HARRY_DUBOIS', 'age': 44}]
df_list_dicts = pd.DataFrame(list_dicts)
print("\nDataFrame из списка словарей:")
print(df_list_dicts)

series_A = pd.Series([1, 2, 3], name="A")
series_B = pd.Series([4, 5, 6], name="B")
df_series_dict = pd.DataFrame({'A': series_A, 'B': series_B})
print("\nDataFrame из словаря объектов Series:")
print(df_series_dict)

numpy_array = np.array([[1, 2], [3, 4], [5, 6]])
df_numpy_array = pd.DataFrame(numpy_array, columns=["Column 1", "Column 2"])
print("\nDataFrame из двумерного массива NumPy:")
print(df_numpy_array)

dtype = [('name', 'U10'), ('age', 'i4')]
struct_array = np.array([('VLADIMIR', 72), ('Donald', 78), ('HARRY_DUBOIS', 44)], dtype=dtype)
df_struct_array = pd.DataFrame(struct_array)
print("\nDataFrame из структурированного массива NumPy:")
print(df_struct_array)
