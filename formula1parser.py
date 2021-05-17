import requests
from bs4 import BeautifulSoup


class FormulaParseRes:
    """
    Class to save result of parsing
    """
    def __init__(self, name, url):
        self.name = name
        self.url = url


class Formula1Parser:
    base_url = 'https://www.formula1.com'
    r = requests.get(base_url + '/en/drivers.html')

    @classmethod
    def get_drivers(cls):
        to_return = []
        bs = BeautifulSoup(cls.r.content, 'html.parser')

        # Find all tags <a> which contains driver
        drivers = bs.find_all('a', class_='listing-item--link')

        for driver in drivers:
            # Find tag which contain driver name
            name = driver.find('div', class_='listing-item--name')
            # And get link fron tag <a>
            link = driver['href']
            # Check if name isn't None
            if name:
                name = name.text
            
            to_return.append(FormulaParseRes(
                str(name).replace('\n', ' '),
                cls.base_url + link))

        return to_return


# # Usage:
# drivers = Formula1Parser.get_drivers()

# for driver in drivers:
#     print(driver.name, driver.url)
