# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv(
    '../data/players_20.csv'
)

for column in df.columns:
    print(column)

# print(df.columns)
print(df.shape)
print(df.describe())

nationalities = df['nationality']

countries = list(nationalities.value_counts(sort=True).to_dict().keys())[:10]
numbers = nationalities.value_counts(sort=True).to_list()[:10]

left = np.array(countries)
height = np.array(numbers)

plt.figure(figsize=(10, 10))
plt.bar(left, height)
plt.title('Players count')
plt.xlabel('Countries')
plt.ylabel('Players count')
plt.grid(True)

plt.show()
