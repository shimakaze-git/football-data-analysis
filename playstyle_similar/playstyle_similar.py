import pandas as pd

from scaling import convert_scaling
from similar import similarity


# ヒートマップの情報を表示
def heatmap_info(player_1_df, player_2_df):

    # 結合処理
    df = player_1_df.append(player_2_df)

    # print(player_1_df.values)
    # print(player_2_df.values)

    # print(df.values)
    print(df.columns)
    print(df)

    df_corr = df.corr(method='kendall')
    print(df_corr)
    # scaling


def columns_views(player_1_df, player_2_df):

    columns = list(player_1_df.columns)
    if list(player_1_df.columns) == list(player_2_df.columns):
        columns = list(player_1_df.columns)

        player_1 = list(player_1_df.values[0])
        player_2 = list(player_2_df.values[0])

        views = []
        for column, player1, player2 in zip(columns, player_1, player_2):
            print('column : {} _ player1-{} , player2-{} < diff : {} >'.format(
                column, player1, player2, abs(player1 - player2)
            ))
            views.append(abs(player1 - player2))

        print(views)


def convert_preferred_foot(df):

    df['preferred_foot'] = df['preferred_foot'].replace('Right', 1)
    df['preferred_foot'] = df['preferred_foot'].replace('Left', 2)

    return df


def convert_work_rate(df):

    convert = {
        'High': 3,
        'Medium': 2,
        'Low': 1
    }

    def convert_attack_value(value):
        attack = value.split('/')[0]
        return convert[attack]

    def convert_defensevalue(value):
        defense = value.split('/')[1]
        return convert[defense]

    df['attack'] = df['work_rate'].map(convert_attack_value)
    df['defense'] = df['work_rate'].map(convert_defensevalue)

    # work_rateの削除処理
    df = df.drop(columns='work_rate')

    return df


# 選手特性を,で分割
def split_trait(value):
    return str(value).split(',')


# 数値型の整形
def shaping_num(value):

    # 一度文字列型に変換する
    value = str(value)

    if '+' in value:
        value = str(value).split('+')
        value = int(value[0]) + int(value[1])
        return value

    if '-' in value:
        value = str(value).split('-')
        value = int(value[0]) - int(value[1])
        return value

    return float(value)


# 必要な列のリストを返す
def need_columns(add_columns=[]):
    columns = [
        'height_cm',
        'weight_kg',
        'preferred_foot',
        'weak_foot',
        'skill_moves',
        'work_rate',
        'player_tags',

        'pace',
        'shooting',
        'passing',
        'dribbling',
        'defending',
        'physic',
        'player_traits',

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

    columns += [
        'ls', 'st', 'rs',
        'lw', 'lf', 'cf', 'rf', 'rw',
        'lam', 'cam', 'ram',
        'lm', 'lcm', 'cm', 'rcm', 'rm',
        'lwb', 'ldm', 'cdm', 'rdm', 'rwb',
        'lb', 'lcb', 'cb', 'rcb', 'rb'
    ]
    # ls,st,rs,lw,lf,cf,rf,rw,
    # lam,cam,ram,lm,lcm,cm,rcm,rm,
    # lwb,ldm,cdm,rdm,rwb,lb,lcb,cb,rcb,rb

    for column in add_columns:
        if column not in columns:
            columns.append(column)

    return columns


def convert_num_values(df):
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

    for v in num_values:
        # データの数値の整形
        values = df[v].map(shaping_num)
        df[v] = values
    return df


def convert_traits(df):

    # 選手特性関連の処理
    traits_list = [
        'Backs Into Player',  # FIFA 18だけの項目
        'Bicycle Kicks',
        'Chip Shot',
        'Dives Into Tackles',
        'Early Crosser',
        'Fancy Passes',
        'Finesse Shot',
        'Flair',
        'Giant Throw-In',
        'GK Cautious With Crosses',
        'GK Comes For Crosses',
        'GK Flat Kick',
        'GK Long Thrower',
        'GK Save With Foot',
        'Injury Prone',
        'Leadership',
        'Long Passer',
        'Long Shot Taker',
        'Long Throw-In',
        'One Club Player',
        'Outside Foot Shot',
        'Play Maker',
        'Playmaker',
        'Power Header',
        'Rushes Out Of Goal',
        'Second Wind',
        'Set Play Specialist',
        'Solid Player',
        'Speed Dribbler',
        'Swerve',
        'Takes Powerful Driven Free Kicks',
        'Team Player',
        'Technical Dribbler'
    ]

    # 選手特性の抽出
    def etract_traits(values):
        values_list = []
        for value in values:
            for trait in traits_list:
                if trait in value:
                    values_list.append(trait)
        return values_list

    df_player_traits = df['player_traits']
    df_values = df_player_traits.map(split_trait)

    for trait in traits_list:
        df[trait] = 0

    for i, values in enumerate(df_values):
        e_values = etract_traits(values)
        for value in e_values:
            # df.loc[i][value] = 1
            df.loc[i, value] = 1

    df = df.drop(columns='player_traits')
    return df


# 補完値の算出
def complementary_value(df, column):
    # 平均値
    missing_value = df[column].mean()
    # print('missing_value', missing_value)

    # 中央値
    # missing_value = df[column].median()

    # https://bellcurve.jp/statistics/blog/14238.html
    # １．欠損値を放置
    # ２．欠損値を含むケースをリストごと削除
    # ３．欠損値に平均値を代入
    # ４．欠損値を含む人と属性の似ている人の値を代入（ hot-deck imputation ）
    # ５．重回帰式などによって値を推計して代入（ cold-deck imputation ）
    # ６．前回の観測値を代入（ LOCF, LVCF ）
    # ７．多重代入法により代入（ multiple imputation ）
    return missing_value


# 欠損値の補完
def missing_values(df):
    for column, count in zip(df.isnull(), df.isnull().sum()):
        if count > 0:
            # 欠損値を算出
            missing_value = complementary_value(df, column)
            df[column].fillna(missing_value, inplace=True)
    return df


# extraction
def df_shaping():
    df = pd.read_csv('../data/players_18.csv')
    df_data = df.copy()

    add_columns = ['sofifa_id']
    df_data = df_data[need_columns(add_columns)]

    return df_data


def players_comparison(player_1, player_2):
    # 整形されたdfの取得
    df = df_shaping()

    # num_valuesの変換処理
    df = convert_num_values(df)

    # 選手特性関連の処理
    df = convert_traits(df)

    # 選手タグ関連の処理
    df = df.drop(columns='player_tags')

    # 利き足の変換
    df = convert_preferred_foot(df)

    # 攻撃/守備の優先度の変換
    df = convert_work_rate(df)

    # 欠損値の補完処理
    df = missing_values(df)

    # 正規化や標準化
    df = convert_scaling(df)

    player_1_df = df.query('sofifa_id == {}'.format(player_1))
    player_2_df = df.query('sofifa_id == {}'.format(player_2))

    player_1_df = player_1_df.drop(columns='sofifa_id')
    player_2_df = player_2_df.drop(columns='sofifa_id')

    # print('player_1_df', player_1_df.values)
    # print('player_2_df', player_2_df.values)

    cos = similarity(player_1_df, player_2_df)
    print('cos', cos)

    # カラムの表示
    # columns_views(player_1_df, player_2_df)

    # 相関度やヒートマップ情報の抽出
    # heatmap_info(player_1_df, player_2_df)


shinji_kagawa = 189358
# david_silva = 192318
# david_silva = 168542
david_silva = 41
# david_silva = 189881
# david_silva = 188152
# 香川真司 : 189358
# 本田圭佑 : 186581
# 清武弘嗣 : 210126
# イニエスタ: 41
# スモーリング : 189881
# セルヒオ・ラモス : 155862
# マリオ・ゲッツェ : 192318
# ユリアン・ヴァイグル : 222028
# ファン・マタ : 178088
# イスコ : 197781
# ダビド・シルバ : 168542
# マルク・バルトラ : 198141
# ロメル・ルカク : 192505
# デブルイネ : 192985
# モドリッチ : 177003
# クロース : 182521
# ラキティッチ : 168651
# ウサマ・デンベレ : 231443
# リオネル・メッシ : 158023
# フンメルス : 178603
# ピケ: 152729
# ボアテング : 183907
# メスト・エジル : 176635
# マルコ・ロイス : 188350
# イヴァン・ペリシッチ : 181458
# トーマス・ミュラー : 189596
# オスカル : 188152
# ヤルモレンコ : 194794
# エデン・アザール : 183277
# ネイマール : 190871
# ロッベン : 9014
# サラー : 209331
# ハリー・ケイン : 202126
# ムバッペ : 231747
# グリーズマン : 194765


players_comparison(shinji_kagawa, david_silva)

# columns_views(shinji_kagawa, david_silva)

# Weak Foot(逆足)
# https://www.fifplay.com/encyclopedia/weak-foot/

# Work Rate(作業率)
# https://www.fifplay.com/encyclopedia/work-rate/

# ユークリッド距離 vs コサイン類似度
# https://enjoyworks.jp/tech-blog/2242