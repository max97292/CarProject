import requests
import json
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Get F1 Driver details')


def get_drivers_data():
    data = requests.get('http://ergast.com/api/f1/drivers.json?limit=10000')
    y = json.loads(data.text)
    drivers_list = y['MRData']['DriverTable']['Drivers']
    return drivers_list

def get_driver_wiki(family_name, given_name):
    for driver in get_drivers_data():
        if (family_name in driver['familyName'] and given_name in driver['givenName']):
            return driver['url']
    print("Driver " + given_name + family_name + " URL not found")
    return None

def table_to_dict(table):
    t_headers = []
    table_row = []
    career = ''
    for th,tr in zip(table.find_all("th"),table.find_all("tr")):
        if(th.has_attr('class')):
            if "infobox-header" in th['class']:
                career = th.text.replace('\n', ' ').strip()
                continue
        if career == "Formula One World Championship career":
            t_headers.append(th.text.replace('\n', ' ').strip())
            for td in tr.find_all("td"): 
                table_row.append(td.text.replace('\n', '').strip())
    a_zip = zip(t_headers , table_row)
    return dict(a_zip)


def scrape_wiki(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find("table",{'class' : 'infobox biography vcard'})
    if table == None:
        table = soup.find("table",{'class' : 'infobox vcard'})
    if table == None:
        print("Driver Data not present in Wiki")
        return None
    return table_to_dict(table)

# Print the statistics of each driver taken from wiki
for driver in get_drivers_data():
    print(driver['familyName'])
    driver_data = scrape_wiki(get_driver_wiki(driver['familyName'], driver['givenName']))
    if len(driver_data) == 0:
        print("Driver has no F1 career")
    print(driver_data)