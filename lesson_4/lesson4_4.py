import pandas as pd

ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['d', 'e', 'f'], index=[4, 5, 6])

print(ser1)

print(ser2)

print(pd.concat([ser1, ser2], axis=1, join='outer'))

print(pd.concat([ser1, ser2], axis=1, join='inner'))
