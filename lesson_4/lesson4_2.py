import pandas as pd
import numpy as np

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)
data = rng.random((4, 6))

df = pd.DataFrame(data, index=index, columns=columns)
print(df)

indxslc = pd.IndexSlice
df_person_1_3 = df.loc[:, indxslc[['person_1', 'person_3'], :]]
print(df_person_1_3)

df_city1_person1_2 = df.loc[indxslc['city_1', :], indxslc[['person_1', 'person_2'], :]]
print(df_city1_person1_2)

df_city2_2020_person2_3_job1 = df.loc[indxslc['city_2', 2020], indxslc[['person_2', 'person_3'], 'job_1']]
print(df_city2_2020_person2_3_job1)