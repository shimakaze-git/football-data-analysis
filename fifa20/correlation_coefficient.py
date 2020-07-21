# -*- coding: utf-8 -*-
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

df

pd.set_option('display.max_rows', 150)

pd

df

pd.set_option('display.max_columns', 150)

df

df.describe()

df.isnull()

df.isnull().any()

df.isnull().sum()

df.isnull().sum()/len(df)

df.isnull().mean()

df.isnull().sum()

df

df['passing'].mean()

df['passing'].mean()

df['passing'].median()()

df['passing'].median()

df.drop(['sofifa_id'])

df.drop(columns=['sofifa_id'])

df.drop(columns=['sofifa_id', 'player_url', 'short_name', 'long_name'])

df.drop(columns=['id'])

df.columns

df.corr()

df

df_corr = df_corr = df.corr()

df_corr

import seaborn as sns

import matplotlib.pyplot as plt

plt.figure()

# +
# sns.heatmap
# -

sns.heatmap(df_corr)

players = df.drop(columns=['sofifa_id', 'player_url', 'short_name', 'long_name'])

players

players = df.drop(columns=['sofifa_id', 'player_url', 'short_name', 'long_name', 'dob'])

players

players.isnull().sum()


def kesson_table(df): 
        null_val = df.isnull().sum()
        percent = 100 * df.isnull().sum()/len(df)
        kesson_table = pd.concat([null_val, percent], axis=1)
        kesson_table_ren_columns = kesson_table.rename(
        columns = {0 : '欠損数', 1 : '%'})
        return kesson_table_ren_columns


kesson_table(players)

players

sns.heatmap(players)

players.corr()

sns.heatmap(players.corr(), annot=True)

sns.heatmap(players.corr(), annot=True)

sns.heatmap(players.corr())

sns.lmplot(..., height=10, aspect=2)

plt.figure(figsize=(12, 9))

sns.heatmap(players.corr())

plt.figure(figsize=(100, 100))

sns.heatmap(players.corr())

plt.figure(figsize=(9, 6)) 
sns.heatmap(players.corr(), square=True)

plt.figure(figsize=(12, 9)) 
sns.heatmap(players.corr(), square=True)

plt.figure(figsize=(30, 20)) 
sns.heatmap(players.corr(), square=True)

players

kesson_table(players)

players['pace'].medium()

players['pace'].median()

players['pace'].mean()

# +
# train["Age"] = train["Age"].fillna(train["Age"].median())
# -

players['pace'] = players['pace'].fillna(players['pace'].mean())

test= list(kesson_table(players))

players['player_tags']

test= list(kesson_table(players))

test

kesson_table(players)

 players['shooting'] = players['shooting'].fillna(players['shooting'].mean())

test = kesson_table(players)


test

test[0]

 players['passing'] = players['passing'].fillna(players['passing'].mean())

players

 kesson_table(players)

df

players = players[players["player_positions"] != GK]

players = players[players["player_positions"] != 'GK']

players

players.query('team_position == "GK"')

players

 kesson_table(players)

field_playesr = players.drop(columns=['gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning'])

plyaers

field_playesr = players.drop(columns=['gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning'])

field_playesr

 kesson_table(field_playesr)

field_playesr.query('nation_position == "GK"')

players['release_clause_eur'] = players['release_clause_eur'].fillna(players['release_clause_eur'].mean())

field_playesr['release_clause_eur'] = field_playesr['release_clause_eur'].fillna(field_playesr['release_clause_eur'].mean())

 kesson_table(field_playesr)

field_playesr.corr()

field_players = players.drop(columns=['gk_diving', 'gk_handling', 'gk_kicking', 'gk_reflexes', 'gk_speed', 'gk_positioning', 'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes'])


field_players['release_clause_eur'] = field_players['release_clause_eur'].fillna(field_players['release_clause_eur'].mean())

field_players

 kesson_table(field_players)

plt.figure(figsize=(30, 20)) 
sns.heatmap(field_players.corr(), square=True)

# +
# , annot=True
# -

plt.figure(figsize=(30, 20)) 
sns.heatmap(field_players.corr(), square=True, annot=True)

df

field_players.corr()['overall'].sort_values()

field_players.corr()['overall'].sort_values()

sns.heatmap(field_players.corr(), vmax=1, vmin=-1, center=0)

plt.figure(figsize=(30, 20)) 
sns.heatmap(field_players.corr(), vmax=1, vmin=-1, center=0, square=True, annot=True)

plt.figure(figsize=(30, 30)) 
sns.heatmap(field_players.corr(), vmax=1, vmin=0, center=0, square=True, annot=True)

plt.figure(figsize=(30, 30)) 
sns.heatmap(field_players.corr(), vmax=1, vmin=0, center=0, square=True, annot=True)

field_players.corr()['overall'].sort_values()

field_players.query('nationality == "Japan"')

df.shape

df.describe()

df.query('age <= 23 & 80 <= potential').query("nationality == 'Japan'")

plt.imshow(df.query('age <= 23 & 80 <= potential').query("nationality == 'Japan'"))
plt.show()

df.isnull().sum()

# 取り出す条件を絞る
field_players = df[df["player_positions"] != 'GK']

# +
gk_drop_list = [
    'gk_diving',
    'gk_handling',
    'gk_kicking',
    'gk_reflexes',
    'gk_speed',
    'gk_positioning',
    'goalkeeping_diving',
    'goalkeeping_handling',
    'goalkeeping_kicking',
    'goalkeeping_positioning',
    'goalkeeping_reflexes'
]

money_drop_list = [
    'value_eur',
    'wage_eur',
    'release_clause_eur'
]

field_players = field_players.drop(columns=gk_drop_list)
field_players = field_players.drop(columns=money_drop_list)
# -

corr = field_players.corr()

# +
# 項目があまりにも多いため、見やすいように画像サイズを大きくする
plt.figure(figsize=(30, 20)) 

# annotにTrueを入れることで相関係数の値を項目に表示する.
sns.heatmap(corr, square=True, annot=True)

plt.show()
# -

corr

corr.value_counts(sort=True)

for c in corr:
        print(c)

corr.corr()['overall'].sort_values()

# +
# sns.pairplot(df_score,hue="性別")

# +
# corr
# -

sns.pairplot(corr)

sns.pairplot(corr, hue='overall')

df

df.query('nationality == "Germany"')

df


