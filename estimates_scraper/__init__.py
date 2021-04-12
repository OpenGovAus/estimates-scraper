from requests import get
from bs4 import BeautifulSoup
from requests.api import head

URL = 'https://www.aph.gov.au/Parliamentary_Business/Senate_estimates/Next_hearings'

def scrape_committees():
    _headers = BeautifulSoup(get(URL).text, 'lxml').find('div', {'_rdeditor_temp': '1'}).find_all('h3')
    _dates = []
    for header in _headers:
        try:
            _dates.append(header.find('br').nextSibling.strip().replace('\xa0', ' '))
        except:
            _dates.append(header.text.replace('\xa0', ' '))
    print(_dates)