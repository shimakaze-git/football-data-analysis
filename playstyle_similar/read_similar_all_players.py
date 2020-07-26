import streamlit as st
import pandas as pd

"""
# similar_all_playersを読みこむ.
データフレームを表として出力できます:
"""


def read_pickle(path=''):
    read_path = path
    if not path:
        read_path = './similar_all_players.pkl'
    df_from_pkl = pd.read_pickle(read_path)

    return df_from_pkl


if __name__ == "__main__":
    df = read_pickle()

    st.dataframe(df)

    """
    # 上位互換を表示.
    player1以上のoverallをもつプレイヤー達を表示する:
    """
    # first = df.iloc[0]
    # first_overall = first['overall']

    overall = st.text_input('総合値を入力', 83)
    similarity = st.text_input('類似度を0~1で入力', 0.85)

    if overall and similarity:
        query_text = 'overall >= {} & similarity >= {}'.format(
            str(overall), str(similarity)
        )
        upper_compatibility = df.query(query_text)
        st.dataframe(upper_compatibility)
