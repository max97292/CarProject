import requests
import json
from bs4 import BeautifulSoup

class GetDriverBio:

    def __init__(self,career="Formula One World Championship career"):

        self.career = career

    @property
    def drivers_data(self):

        data = requests.get('http://ergast.com/api/f1/drivers.json?limit=10000')
        y = json.loads(data.text)
        drivers_list = y['MRData']['DriverTable']['Drivers']
        return drivers_list

    def get_driver_wiki(self, family_name, given_name):

        for driver in self.drivers_data:
            if (family_name.lower() in driver['familyName'].lower() and given_name.lower() in driver['givenName'].lower()):
                return driver['url']
        print("Driver " + given_name + family_name + " URL not found")
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
                for td in tr.find_all("td"): 
                    table_row.append(td.text.replace('\n', '').strip())
        a_zip = zip(t_headers , table_row)
        return dict(a_zip)


    def wiki_stats_to_dict(self,url):

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find("table",{'class' : 'infobox biography vcard'})
        if table == None:
            table = soup.find("table",{'class' : 'infobox vcard'})
        if table == None:
            return None
        return self.table_to_dict(table)

    def get_all_driver_data(self):
        for driver in self.drivers_data:
            driver_dat = self.wiki_stats_to_dict(self.get_driver_wiki(driver['familyName'], driver['givenName']))
            if driver_dat == None:
                print("Driver Data not present in Wiki")
                continue
            if len(driver_dat) == 0:
                print("Driver has no F1 career")
                continue
            driver_dat["familyName"] = driver['familyName']
            driver_dat["givenName"] = driver['givenName']
            driver_dat["dateOfBirth"] = driver['dateOfBirth']
            print(driver_dat)

# Usage
drvbio = GetDriverBio()
drvbio.get_all_driver_data()