import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp


class Formula1Parser:
    base_url = 'https://www.formula1.com'

    @classmethod
    def get_links(cls):
        r = requests.get(cls.base_url + '/en/drivers.html')
        bs = BeautifulSoup(r.content, 'html.parser')

        # Find all tags <a> which contains driver
        drivers = bs.find_all('a', class_='listing-item--link')

        for driver in drivers:
            yield driver['href']

    @staticmethod
    def table_to_dict(table):
        t_headers = []
        table_row = []

        for th, td in zip(table.find_all("th"), table.find_all("td")):
            t_headers.append(th.span.text.lower())
            table_row.append(td.text)

        return dict(zip(t_headers, table_row))

    @classmethod
    def get_drivers(cls):
        for driver_link in cls.get_links():
            driver_dict = {}
            bio = ''

            r = requests.get(cls.base_url + driver_link)
            bs = BeautifulSoup(r.content, 'html.parser')

            driver_name = bs.find('h1', class_='driver-name').text
            # table = zip(bs.find_all('th'), bs.find_all('td'))
            table = bs.find('table', class_='stat-list')

            driver_dict.update({'name': driver_name})

            for div in bs.find('section', class_='biography').find_all('div'):
                if div.text:
                    bio += div.text.replace('\n', ' ').strip()

            driver_dict.update({'bio': bio})

            driver_dict.update(cls.table_to_dict(table))

            yield driver_dict


# # Usage
# for driver_data in Formula1Parser.get_drivers():
#     pp(driver_data)
