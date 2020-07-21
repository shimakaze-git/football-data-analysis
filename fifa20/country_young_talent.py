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

# +
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
# -

df = pd.read_csv(
    '../data/players_20.csv'
)

# df

# df.columns

# list(df.columns)

# ten_young = df.query('age < 20 & 80 <= potential')

# ten_young

# teens = df.query('age < 20 & 80 <= potential')

# teens_nationalities = teens['nationality']

# teens_nationalities

# teens_nationalities.value_counts(sort=True).to_dict()

# df.query('age < 20 & 80 <= potentia & nationality == "Japan"l')

# df.query('age < 20 & 80 <= potentia & nationality == Japanl')

# df.query('age < 20 & 80 <= potentia').query('nationality = Japanl')

# df.query('age < 20 & 80 <= potentia').query('nationality == Japanl')

# df.query('age < 20 & 80 <= potentia')

# df.query('age < 20 & 80 <= potential')

# df.query('age < 20 & 80 <= potential').query('nationality == Japan')

# df.query('age < 20 & 80 <= potential').query("nationality == 'Japan'")

# df.query('age < 20 & 75 <= potential').query("nationality == 'Japan'")

# pd.get_option("display.max_columns")

# df.query('age < 20 & 75 <= potential').query("nationality == 'Japan'")

# pd.set_option('display.max_rows', 150)

# df.query('age < 20 & 75 <= potential').query("nationality == 'Japan'")

# pd.set_option('display.max_columns', 150)

# df.query('age < 20 & 75 <= potential').query("nationality == 'Japan'")z

# df.query('age < 20 & 75 <= potential').query("nationality == 'Japan'")

# df.query('age <= 24 & 75 <= potential').query("nationality == 'Japan'")

# df.query('age <= 24 & 80 <= potential').query("nationality == 'Japan'")

# df.query('age <= 23 & 75 <= potential').query("nationality == 'Japan'")

# df.query('age <= 23 & 80 <= potential').query("nationality == 'Japan'")

# teens_nationalities

# teens = df.query('age < 20 & 80 <= potential')

# teens

# teens['nationality'].value_counts(sort=True).to_dict()

# twenties= df.query('20 <= age & age < 30 & 80 <= potential')

# twenties

# twenties['nationality'].value_counts(sort=True).to_dict()

# twenties.query("nationality == 'Japan'")

# twenties_countries = list(twenties.value_counts(sort=True).to_dict().keys())[:10]
# twenties_numbers = twenties.value_counts(sort=True).to_list()[:10]

# twenties.value_counts(sort=True)

# twenties

# twenties_countries = list(twenties['nationality'].value_counts(sort=True).to_dict().keys())[:10]
# twenties_numbers = twenties['nationality'].value_counts(sort=True).to_list()[:10]

# twenties_countries

# twenties_numbers

# left = np.array(countries)
# height = np.array(numbers)

# left = np.array(twenties_countries)
# height = np.array(twenties_numbers)

# plt.bar(left, height)
# plt.title('Players count')
# plt.xlabel('Countries')
# plt.ylabel('Players count')
# plt.grid(True)

young_talents = df.query('age <= 23 & 80 <= potential')

# nationalityで国籍の列を取り出す
nationalities = young_talents['nationality']

# 標準出力結果
print(nationalities.value_counts(sort=True).to_dict())

# value_countsでそれぞれの要素数をカウントする
# これで国ごとの選手数が集計される
countries = list(nationalities.value_counts(sort=True).to_dict().keys())[:10]
numbers = nationalities.value_counts(sort=True).to_list()[:10]

left = np.array(countries)
height = np.array(numbers)


# matplotlibによるグラフの描写
# 画像サイズが小さくて収まらないのでfgureで画像サイズを大きくしています.

plt.figure(figsize=(10, 10))

plt.bar(left, height)
plt.title('Players count')
plt.grid(True)

plt.show()