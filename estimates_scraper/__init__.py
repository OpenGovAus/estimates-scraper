from requests import get
from bs4 import BeautifulSoup
from requests.api import head

URL = 'https://www.aph.gov.au/Parliamentary_Business/Senate_estimates/Next_hearings'

def scrape_committees():
    _soup = BeautifulSoup(get(URL).text, 'lxml')
    YEAR = _soup.find('span', {'class': 'not-bold'}).find('br').nextSibling.strip()[-4:]
    _headers = _soup.find('div', {'_rdeditor_temp': '1'}).find_all('h3')
    hearing_list = []
    for header in _headers:
        portfolios = []
        for comm in header.findNext('div').find_all('div', {'class': 'box'}):
            for comm_name in comm.find('ul').find_all('li'):
                portfolios.append(comm_name.text)
            print(portfolios)
        
        try:
            _date = header.find('br').nextSibling.strip().replace('\xa0', ' ')
        except:
            _date = header.text.replace('\xa0', ' ')
        hearing_list.append({'date': _date, 'portfolios': portfolios})
    return hearing_list
        