import requests
from proxy import get_proxy


def get_html(url):

    p = get_proxy()
    
    try:
        
        proxy = { p['schema']: p['address'] }
        r = requests.get(url, proxies=proxy, timeout=5)
        
        print('Now used ' + p['schema'] + ' ' + p['address'])
        
        return r
    
    except:
        
        r = requests.get(url)
        
        print('The site did not provide https proxy, so now your proxy is used')

        return r
