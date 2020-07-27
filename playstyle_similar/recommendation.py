import numpy as np
from scipy.spatial.distance import (
    correlation,
    cosine,
    pdist,
    cdist
)
from scipy import stats


# cos類似度
def cos_similarity(item1, item2):
    return 1 - cosine(item1, item2)


# scipyによるPearsonの(積率)相関係数
def distance_correlation(x, y):
    return 1 - correlation(x, y)


# ピアソンの積率相関係数
def pearson_product_moment_correlation_coefficien(v1, v2):
    corr = stats.pearsonr(v1, v2)

    return corr[0]


# p値も算出する
def stats_pearsonr(x, y):
    return stats.pearsonr(x, y)[0]


# item1とitem2の類似度を算出する
def _similarity(item1, item2):
    similarity_value = cos_similarity(item1, item2)
    return similarity_value


# 距離行列を算出する
# xの行数がNの場合はN*(N-1)/2
def _pdist(x):
    # d = pdist(x, 'cosine')
    d = pdist(x, distance_correlation)
    return d


# 2つのデーターセット間の距離行列を算出する
def _cdist(x_A, x_B):
    d = cdist(x_A, x_B, distance_correlation)
    return d


# dfはpandasの行列
def _recommendation(df, idx):
    df_data = df.drop(columns='sofifa_id')

    df_values = df_data.values

    # 一人のプレイヤーの行を抽出する
    main_player = df_values[idx]
    main_player = np.array([main_player])

    d = _cdist(main_player, df_values)
    return d
