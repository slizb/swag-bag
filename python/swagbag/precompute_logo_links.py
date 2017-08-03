from bs4 import BeautifulSoup
import requests
import pickle
import numpy as np

df = pickle.load(open("../data/team_color_frame.pkl", "rb"))
df['logo_url'] = np.nan

leagues = df.league.unique()


def teams_in_league(league):
    return df.name[df.league == league]


def extract_logo_link_from_page(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    logo_link = soup.find_all('iframe')[0].get('src')
    return logo_link


for league in leagues:
    for team in teams_in_league(league):
        collapsed_team = team.lower().replace(' ', '-')
        url_prefix = "https://github.com/jimniels/teamcolors/blob/master/static/img/"
        git_url = url_prefix + league + "/" + collapsed_team + ".svg"
        raw_url = extract_logo_link_from_page(git_url)

        row_index = df[df.name == team].index
        df = df.set_value(index=row_index,
                          col='logo_url',
                          value=raw_url)
        print(league, team, ":", raw_url)

df.to_pickle('../data/team_color_frame.pkl')
