import requests

from random import choice
from bs4 import BeautifulSoup


def get_proxy():
    
    html = requests.get('https://free-proxy-list.net/').text
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', id='proxylisttable').find_all('tr')[1:21]

    proxies = []

    for tr in trs:
        
        tds = tr.find_all('td')
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        schema = 'https' if 'yes' in tds[6].text.strip() else 'http'
        proxy = {'schema': schema, 'address': ip + ':' + port}

        if proxy['schema'] == 'https':
            proxies.append(proxy)
            
    try:        
        return choice(proxies)
    
    except:        
        return proxies
