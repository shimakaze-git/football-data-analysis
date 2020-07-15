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

import pandas as pd

pipenv install pandas

pip install pandas

pip list

# cat Pipfile

import pandas as pd

pd


df = pd.read_csv('data/players_20.csv')

print(df.columns)

print(df)

for column in df.columns:
    print(column)

pd.read_csv('iris.data', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

file = 'data/players_20.csv'
pd.read_csv(file, names=['short_name', 'long_name', 'age', 'club'])

iris = pd.read_csv(file)

iris

iris['age']

iris[['short_name', 'long_name', 'age', 'club']]

df.columns

df.query('nationality == Japan')

df.query('nationality == japan')

df

df.query('age < 25')

df.query('nationality == "Japan"')

df[(df['nationality'] < 'Japan') & (df['overall'] > 75)]

df[(df['nationality'] == 'Japan') & (df['overall'] > 75)]

df[(df['nationality'] < 'Japan') & (df['overall'] > 70)]

df[(df['nationality'] == 'Japan') & (df['overall'] > 70)]

japan_players = df[df['nationality'] == 'Japan')]

japan_players = df[(df['nationality'] == 'Japan')]

japan_players

japan_players['overall']

japan_players.columns

for column in japan_players.columns:
    print(column)

japan_players.query('potential > 80')

japan_players.query('potential > 80')[['short_name'],['potential']]

japan_players.query('potential > 80')[['short_name', 'potential']]

japan_players

japan_players['age'].mean()

japan_players['dribbling'].mean()

japan_players.sort_values('overall', ascending=False)

japan_players.sort_values('overall', ascending=False)

japan_players.sort_values('potential', ascending=False)

japan_players.sort_values('potential', ascending=False)

japan_players.sort_values('potential', ascending=False).head()

japan_players[['short_name', 'long_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur']]

japan_players[['short_name', 'long_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur']]

japan_players[['short_name', 'long_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur']].head(10)

japan_players[['short_name', 'long_name', 'age', 'overall', 'potential', 'value_eur', 'wage_eur', 'club']].head(10)

japan_players.describe()

pd.get_option("display.max_columns")

japan_players.get_option("display.max_columns")


japan_players

pd.set_option('display.max_columns', 104)

japan_players


