import pandas as pd
import numpy as np

rng = np.random.default_rng()

dfA = pd.DataFrame(rng.integers(0, 10, (2, 2)), columns=['a', 'b'])
dfB = pd.DataFrame(rng.integers(0, 10, (3, 3)), columns=['a', 'b', 'c'])

print(dfA)

print(dfB)

result = dfA + dfB

result_fillna = result.fillna(1)

print(result_fillna)
