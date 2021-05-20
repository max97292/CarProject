import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint as pp
from collections import defaultdict

class GetRaceDetails:

    def __init__(self, season="2011", round="5"):

        self.season = season
        self.round = round

    @property
    def f1_races(self):

        races_list = []
        for i in [1,1000]:
            data = requests.get(
                'http://ergast.com/api/f1.json?limit=1000&offset={}'.format(i))
            y = json.loads(data.text)
            races_list = races_list + (y['MRData']['RaceTable']['Races'])
             
        return races_list

    def get_lap_details(self, season, round):

        lap_details = {}
        if(int(season) >= 1996):
            data = requests.get(
                'http://ergast.com/api/f1/{}/{}/laps.json?limit=10000'.format(season, round))
            y = json.loads(data.text)['MRData']['RaceTable']["Races"][0]
            lap_details['Circuit'] = y['Circuit']['circuitId']
            lap_details['Laps'] = y['Laps']
        return lap_details

    def table_to_dict(self, table):

        t_headers = []
        table_row = []
        race_detail = ''
        for tr in table.find_all("tr"):
            for th in tr.find_all("th"):
                if ("race details" in (th.text.replace('\n', ' ').strip()).lower() and len(th.find_next_siblings("td")) == 0):
                    race_detail = th.text.replace('\n', ' ').strip()
                    continue
                if ("race details" not in (th.text.replace('\n', ' ').strip()).lower() and len(th.find_next_siblings("td")) == 0):
                    race_detail = ''
                    break
                if ("race details" in race_detail.lower()):
                    t_headers.append(th.text.replace('\n', ' ').strip())
                    for td in tr.find_all("td"):
                        table_row.append(td.text.replace('\n', '').strip())
        a_zip = zip(t_headers , table_row)
        return dict(a_zip)

    def wiki_stats_to_dict(self, url):

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find("table", {'class': 'infobox vevent'})
        if table == None:
            return None
        return self.table_to_dict(table)

    def get_season_details(self, season, round):

        round_dict = {}
        for race in self.f1_races:
            if race['season'] == str(season) and race['round'] == str(round):
                round_dict = self.wiki_stats_to_dict(race["url"])
                round_dict["RaceName"]  = race["raceName"]
                round_dict["circuitId"] = race['Circuit']["circuitId"]
        return round_dict

# # Usage
# x = GetRaceDetails()
# print(x.get_season_details(2020,5))