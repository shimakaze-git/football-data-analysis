import pandas as pd
from sklearn import preprocessing


# 外れ値に頑健な標準化
# 変換前のデータに極端に大きな値または小さな値が含まれていた場合、
# 標準化を行うと大きく結果が変わってしまう。
# これを避けるため、データの四分位点を基準にして標準化を行う。
def robust_scaler(df, columns):

    # Y= (X − Q2) / (Q3 − Q1)

    # Yは変換後のデータ、Xは変換前のデータ
    # Q1,Q2,Q3は、それぞれXの第1～第3四分位点である。
    # 標準化と比較すると、元のデータの平均がQ2（中央値）、分散がQ3−Q1であると仮定している

    # with_centering
    # ブール型。デフォルト値はTrue.
    # Trueの場合、データから中央値を引いて、平均を0とする。

    # with_std
    # ブール型。デフォルト値はTrue.
    # Trueの場合、quantile_rangeで選択した
    # パーセンタイルのデータの差でデータを割る。

    # quantile_range
    # タプル型。デフォルト値は(25.0, 75.0).
    # 標準化を行うデータの範囲をパーセンテージで指定する。
    # (25.0, 75.0)の場合、下位25%と上位25%にある値の差でデータ全体を割る。
    # また、特徴量が複数ある場合、それぞれの特徴量に対して数値が選ばれる。
    # なお、データの値は、NumPyのpercentile関数で取得している。
    # この関数は、パーセンタイルとデータ数が一致しない場合、補間して返す。
    # そのため、データ数が少ない場合や、離散的な場合は注意する。

    # copy
    # ブール型。デフォルト値はTrue.
    # Falseの場合、transformやfit_transformメソッドで変換時に、
    # 変換元のデータを破壊的に変換する。
    # Trueの場合、元のデータは変換されない。

    rscaler = preprocessing.RobustScaler(
        with_centering=True,
        with_scaling=True,
        quantile_range=(25.0, 75.0),
        copy=True
    )

    rscaler.fit(df)
    data_RobustScaler = rscaler.transform(df)

    data_RobustScaler = pd.DataFrame(
        data_RobustScaler,
        columns=df.columns
    )

    # 置き換え
    df[columns] = data_RobustScaler[columns]
    return df


# 正規化（最大1, 最小0）する
# データの最大値と最小値を制限する変換を正規化と呼ぶ。
def minmax_scaler(df, columns):

    # データの最大値と最小値を制限する変換を正規化と呼ぶ。
    # 最大値を1, 最小値を0とすることが多い。

    # Y = (X − x_min) / (x_max − x_min)

    # feature_range
    # タプル型。デフォルト値は(0, 1).
    # 変換後の最大値、最小値を設定する。

    # copy
    # ブール型。デフォルト値はTrue.
    # Falseの場合、transformやfit_transformメソッドで変換時に、
    # 変換元のデータを破壊的に変換する。
    # Trueの場合、元のデータは変換されない。

    scaler = preprocessing.MinMaxScaler(feature_range=(0, 1), copy=True)

    scaler.fit(df)
    data_MinMaxScaler = scaler.transform(df)

    data_MinMaxScaler = pd.DataFrame(
        data_MinMaxScaler,
        columns=df.columns
    )

    # 置き換え
    df[columns] = data_MinMaxScaler[columns]
    return df


# 標準化（平均0, 分散1）する
# データの平均値と分散を変換する操作を標準化と呼ぶ。
# 平均値を0, 分散を1とすることが多い。
def standard_scaler(df, columns):

    # copy
    # ブール型。デフォルト値はTrue.
    # Falseの場合、transformやfit_transformメソッドで変換時に、
    # 変換元のデータを破壊的に変換する。
    # Trueの場合、元のデータは変換されない。

    # with_mean
    # ブール型。デフォルト値はTrue.
    # Trueの場合、平均値を0とする。
    # Falseの場合、以下の変換になる。
    # Y = X / σ
    # 分散は1になるが、平均は同じままとは限らない。

    # with_std
    # ブール型。デフォルト値はTrue.
    # Trueの場合、分散を0とする。
    # Falseの場合、以下の変換になる。
    # Y = X − μ
    # 分散は変化せず、平均は0となる。

    scaler = preprocessing.StandardScaler(
        copy=True, with_mean=True, with_std=True
    )

    # 配列dfの平均と分散を計算して、記憶する（変換は行わない）。
    scaler.fit(df)

    # 配列dfに変換を施して、変換後の配列を返す。
    data_StandardScaler = scaler.transform(df)

    # 配列dfに対して、fitとtransformを同時に行う。
    # scaler.transform(df)

    data_StandardScaler = pd.DataFrame(
        data_StandardScaler,
        columns=df.columns
    )

    # 置き換え
    df[columns] = data_StandardScaler[columns]
    return df


def frequency_encoding(df, column):

    column_counts = '{}_counts'.format(column)

    # 各カテゴリーの出現回数を計算
    grouped = df.groupby(column).size().reset_index(name=column_counts)

    # 元のデータセットにカテゴリーをキーとして結合
    df = df.merge(
        grouped,
        how="left",
        on=column
    )
    df[column] = df[column_counts] / df[column_counts].count()
    df = df.drop(columns=column_counts)

    # はじめてのFeature Engineering
    # https://mikebird28.hatenablog.jp/entry/2018/05/19/213047

    # モデリングのための特徴量の前処理について整理した
    # https://ishitonton.hatenablog.com/entry/2019/02/24/184253

    return df


# 正規化や標準化
def convert_scaling(df):

    # 身長を標準化
    df = standard_scaler(df, ['height_cm'])
    # df = robust_scaler(df, ['height_cm'])

    num_values = [
        'pace',
        'shooting',
        'passing',
        'dribbling',
        'defending',
        'physic',
        'attacking_crossing',
        'attacking_finishing',
        'attacking_heading_accuracy',
        'attacking_short_passing',
        'attacking_volleys',
        'skill_dribbling',
        'skill_curve',
        'skill_fk_accuracy',
        'skill_long_passing',
        'skill_ball_control',
        'movement_acceleration',
        'movement_sprint_speed',
        'movement_agility',
        'movement_reactions',
        'movement_balance',
        'power_shot_power',
        'power_jumping',
        'power_stamina',
        'power_strength',
        'power_long_shots',
        'mentality_aggression',
        'mentality_interceptions',
        'mentality_positioning',
        'mentality_vision',
        'mentality_penalties',
        'mentality_composure',
        'defending_marking',
        'defending_standing_tackle',
        'defending_sliding_tackle'
    ]

    num_values += [
        'ls', 'st', 'rs',
        'lw', 'lf', 'cf', 'rf', 'rw',
        'lam', 'cam', 'ram',
        'lm', 'lcm', 'cm', 'rcm', 'rm',
        'lwb', 'ldm', 'cdm', 'rdm', 'rwb',
        'lb', 'lcb', 'cb', 'rcb', 'rb'
    ]

    # 最大値が決まっているものなどを正規化
    minmax_scaler_list = [
        'weight_kg',

        'weak_foot',
        'skill_moves'
    ]
    minmax_scaler_list += num_values

    # カテゴリをスケーリング
    df = minmax_scaler(
        df, minmax_scaler_list
    )

    # カテゴリをスケーリングする
    frequency_encoding_list = [
        'preferred_foot',  # 利き足
        'attack',  # 攻撃優先度
        'defense'  # 守備優先度
    ]
    for category in frequency_encoding_list:
        # カテゴリをスケーリング
        df = frequency_encoding(
            df, category
        )

    return df
