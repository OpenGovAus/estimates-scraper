from requests import get
from bs4 import BeautifulSoup
from requests.api import head
import datetime

URL = 'https://www.aph.gov.au/Parliamentary_Business/Senate_estimates/Next_hearings'


my_months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

class WhatDateError(Exception):
    pass

def convert_to_ios_date(date_string: str, year: int = 2021):
    date_string_list = date_string.split()[1:]
    date_string_list = date_string_list # keeping this for fun
    if date_string_list[0] in my_months.keys():
        return(datetime.date(year, my_months[date_string_list[0]], int(date_string_list[1])))
    elif  date_string_list[1] in my_months.keys():
        return(datetime.date(year, my_months[date_string_list[1]], int(date_string_list[0])))
    else:
        raise WhatDateError(f"can't identify the date: {date_string}")

def scrape_committees():
    _soup = BeautifulSoup(get(URL).text, 'lxml')
    YEAR = _soup.find('span', {'class': 'not-bold'}).find('br').nextSibling.strip()[-4:]
    _headers = _soup.find('div', {'_rdeditor_temp': '1'}).find_all('h3')
    hearing_list = []
    for header in _headers:
        portfolios = []
        for comm in header.findNext('div').find_all('div', {'class': 'box'}):
            _committee = comm.find('strong').text
            for comm_name in comm.find('ul').find_all('li'):
                portfolios.append(comm_name.text)
        _date = ""
        try:
            _date = convert_to_ios_date(header.find('br').nextSibling.strip().replace('\xa0', ' '))
        except:
            _date = convert_to_ios_date(header.text.replace('\xa0', ' '))

        hearing_list.append({'committee': _committee, 'date': str(_date), 'portfolios': portfolios})
    return hearing_list
        
