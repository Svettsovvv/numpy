import pandas as pd

index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

pop = pd.Series(population, index=index)

pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)

print(pop_df)

pop_df_1 = pop_df.loc[('city_1', slice(None)), 'something']
print(pop_df_1)

pop_df_1 = pop_df.loc[[('city_1', 'city_3')], ['total', 'something']]
print(pop_df_1)

