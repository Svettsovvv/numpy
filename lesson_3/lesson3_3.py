import numpy as np
import pandas as pd

data = {
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, np.nan, 4, 5],
    'C': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

print(df)

df_f = df.ffill()
print(df_f)

df_b = df.bfill()
print(df_b)
