import requests
import pandas as pd

from bs4 import BeautifulSoup


def fetch_league_country(soup):
    bp3_card_player = soup.find(class_='bp3-card player')
    info = bp3_card_player.find('div', class_='info')
    meta = info.find('div', class_='meta bp3-text-overflow-ellipsis')
    league_country = meta.find('a')['title']
    return league_country


def fetch_team_name(soup):
    flex_centered_header = soup.find(class_='flex-centered header')
    team_name = flex_centered_header.find('h1', class_='bp3-text-overflow-ellipsis')

    return team_name.text


def fetch_team_info(res):
    soup = BeautifulSoup(res, 'html.parser')

    team_name = fetch_team_name(soup)
    league_country = fetch_league_country(soup)

    return team_name, league_country


def scraiping_team_name(path):
    url = 'https://sofifa.com/team/' + str(path)
    res = requests.get(url).text

    team_name, league_country = fetch_team_info(res)
    return team_name, league_country


def save_csv(data_list, columns, save_path):
    # データフレームを作成
    df = pd.DataFrame(data_list, columns=columns)

    # CSV ファイルとして出力
    df.to_csv(save_path)


if __name__ == "__main__":
    df = pd.read_csv('data/teams_and_leagues.csv', sep=',')

    data_list = []
    for index, row in df.iterrows():

        url = row['url']
        league_name = row['league_name']

        team_name, league_country = scraiping_team_name(url)
        print('team_name, league_country', team_name, league_country)

        data_list.append([url, league_name, team_name, league_country])

    columns = ['url', 'league_name', 'team_name', 'league_country']
    save_csv(data_list, columns, 'data/team_infos.csv')
