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

def convert_to_ios_date(date_string: str, year: int = 2021):
    date_string_list = date_string.split()
    return(datetime.date(year, my_months[date_string_list[2]], int(date_string_list[1])))

def scrape_committees():
    _headers = BeautifulSoup(get(URL).text, 'lxml').find('div', {'_rdeditor_temp': '1'}).find_all('h3')
    _dates = []
    for header in _headers:
        try:
            date_string = header.find('br').nextSibling.strip().replace('\xa0', ' ')
            _dates.append(date_string)
            print(convert_to_ios_date(date_string))

        except:
            _dates.append(header.text.replace('\xa0', ' '))
    # print(_dates)