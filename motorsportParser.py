import requests
from bs4 import BeautifulSoup


class MotorsportsParseRes:
    """
    Class to save result of parsing
    """

    def __init__(self, name, url):
        self.name = name
        self.url = url


class MotorsportParser:
    base_url = 'https://results.motorsportstats.com'
    r = requests.get(base_url + '/drivers')

    @classmethod
    def get_drivers(cls):
        to_return = []
        bs = BeautifulSoup(cls.r.content, 'html.parser')

        # Find all tags <div> which contains driver
        drivers = bs.find_all('div', class_='slick-slide slick-active')

        for driver in drivers:
            link = driver.find('a')
            if link:
                name = link.find('div').text
                link = cls.base_url + link['href']
                to_return.append(MotorsportsParseRes(name, link))

        return to_return

# Usage:
drivers = MotorsportParser.get_drivers()

for driver in drivers:
    print(driver.name, driver.url)