import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint as pp

class GetDriverBio:

    def __init__(self, career="Formula One World Championship career"):

        self.career = career

    @property
    def drivers_data(self):

        data = requests.get(
            'http://ergast.com/api/f1/drivers.json?limit=1000')
        y = json.loads(data.text)
        drivers_list = y['MRData']['DriverTable']['Drivers']
        return drivers_list

    def get_driver_standings(self, family_name, given_name):

        driver_id = self.get_driver_id(family_name, given_name)
        data = requests.get(
            'http://ergast.com/api/f1/drivers/{}/driverStandings.json?limit=1000'.format(driver_id))
        y = json.loads(data.text)
        driver_standings_list = y['MRData']['StandingsTable']['StandingsLists']
        return driver_standings_list

    def get_driver_constructors(self, family_name, given_name):

        driver_id = self.get_driver_id(family_name, given_name)
        data = requests.get(
            'http://ergast.com/api/f1/drivers/{}/constructors.json?limit=1000'.format(driver_id))
        y = json.loads(data.text)
        driver_constructors_list = y['MRData']['ConstructorTable']['Constructors']
        return driver_constructors_list

    def get_driver_wiki(self, family_name, given_name):

        for driver in self.drivers_data:
            if (family_name.lower() in driver['familyName'].lower() and given_name.lower() in driver['givenName'].lower()):
                return driver['url']
        print("Driver " + given_name + family_name + " URL not found")
        return None

    def get_driver_id(self, family_name, given_name):

        for driver in self.drivers_data:
            if (family_name.lower() in driver['familyName'].lower() and given_name.lower() in driver['givenName'].lower()):
                return driver['driverId']
        print("Driver " + given_name + family_name + " driverId not found")
        return None

    def table_to_dict(self, table):

        t_headers = []
        table_row = []
        career = ''
        for th,tr in zip(table.find_all("th"),table.find_all("tr")):
            if(th.has_attr('class')):
                if "infobox-header" in th['class']:
                    career = th.text.replace('\n', ' ').strip()
                    continue
            if career == self.career:
                t_headers.append(th.text.replace('\n', ' ').strip())
                for td in th.find_next_siblings("td"):
                    table_row.append(td.text.replace('\n', '').strip())
        a_zip = zip(t_headers , table_row)
        return dict(a_zip)

    def wiki_stats_to_dict(self, url):

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find("table", {'class': 'infobox biography vcard'})
        if table == None:
            table = soup.find("table", {'class': 'infobox vcard'})
        if table == None:
            return None
        return self.table_to_dict(table)

    def get_all_driver_data(self):

        for driver in self.drivers_data:
            driver_dat = self.wiki_stats_to_dict(
                self.get_driver_wiki(driver['familyName'], driver['givenName']))
            if driver_dat == None:
                print("Driver Data not present in Wiki")
                continue
            if len(driver_dat) == 0:
                print("Driver has no F1 career")
                continue
            driver_dat["Name"] = f"{driver['givenName']} {driver['familyName']}"
            driver_dat["dateOfBirth"] = driver['dateOfBirth']
            driver_dat["Nationality"] = driver['nationality']
            driver_dat["driverId"] = driver['driverId']
            driver_dat["Standings"] = self.get_driver_standings(driver['familyName'], driver['givenName'])
            driver_dat["Constructors"] = self.get_driver_constructors(driver['familyName'], driver['givenName'])
            
            yield driver_dat


# # Usage
# drvbio = GetDriverBio()
# for driver_data in drvbio.get_all_driver_data():
#     pp(driver_data)