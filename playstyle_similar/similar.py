# import pandas as pd
import numpy as np

from scipy import stats


def euclidean_distance(v1, v2):
    # ユーグリッド距離を算出
    # https://qiita.com/shim0mura/items/64918dad83d162ef2ac2#ユークリッド距離

    # どちらも同じ値を返す
    # distance = np.linalg.norm(v1 - v2)
    distance = np.sqrt(np.power(v1 - v2, 2).sum())

    # 0から1までの値で似ていれば似ているほど1に近くなる、みたいな類似度として分かりやすい値が欲しい。
    # 0での除算エラーを防ぐためにこのdに1を足して逆数をとるとそのような値を取ることが出来る。
    # 1/(1+d)

    # print('distance', distance)

    return 1 / (1 + distance)


def cos_similarity(v1, v2):
    # Scipyを使ってコサイン類似度を求める方法
    # import scipy.spatial.distance as dis

    # print(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    # print(dis.cosine(v1, v2))

    # return dis.cosine(v1, v2)

    # cos類似度を算出
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


# ピアソンの積率相関係数
def pearson_product_moment_correlation_coefficien(v1, v2):
    # corr = np.corrcoef(v1, v2)[0, 1]
    corr = stats.pearsonr(v1, v2)

    return corr


# スピアマンの順位相関係数
def spearman_rank_correlation_coefficient(v1, v2):
    corr = stats.spearmanr(v1, v2)

    return corr


# ケンドールの順位相関係数
def kendalltau_rank_correlation_coefficient(v1, v2):
    corr = stats.kendalltau(v1, v2)

    return corr


def similarity(v1_df, v2_df):
    v1_value = v1_df.values[0]
    v2_value = v2_df.values[0]

    # リストをps.Seriesに変換
    # s1 = pd.Series(list(v1_value))
    # s2 = pd.Series(list(v2_value))

    # 相関係数を計算
    # res = s1.corr(s2)
    # print(res)

    corr = pearson_product_moment_correlation_coefficien(
        v1_value, v2_value
    )
    # print('pearson_product_moment_correlation_coefficien', corr)

    # corr = spearman_rank_correlation_coefficient(
    #     v1_value, v2_value
    # )
    # print('spearman_rank_correlation_coefficient', corr)

    # corr = kendalltau_rank_correlation_coefficient(
    #     v1_value, v2_value
    # )
    # print('kendalltau_rank_correlation_coefficient', corr)

    # e_distance = euclidean_distance(v1_value, v2_value)
    # print('e_distance', e_distance)

    # cos_similarity_val = cos_similarity(v1_value, v2_value)
    # print('cos_similarity_val', cos_similarity_val)

    return corr
