import requests
import time
from datetime import datetime
import bs4


def parse():

    val = input('Enter your value:').upper()
    headers = {
        'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 "
            "Safari/537.36 Edge/18.19582 "
    }
    params = ['PD', 'ZUO', 'PINS', 'ZM', 'DOCU', 'CLDR', 'RUN']
    if val in params:
        period1 = int(datetime(1970, 1, 1).timestamp())
        period2 = int(datetime.now().timestamp())
        interval: str = '1d'
        url = f'https://query1.finance.yahoo.com/v7/finance/download/{val}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true '
        r = requests.get(url, headers=headers)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        print(soup.text)
    else:
        print('Not supported ticket, make right request!!!')


if __name__ == '__main__':
    parse()
