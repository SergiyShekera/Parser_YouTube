import requests
import csv
import sys
import re

from bs4 import BeautifulSoup
from Proxy import get_proxy


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def get_html(url):

    p = get_proxy()
    
    try:
        
        proxy = { p['schema']: p['address'] }
        r = requests.get(url, proxies=proxy)
        
        print('Now used ' + p['schema'] + ' ' + p['address'])
        
        return r
    
    except:
        
        r = requests.get(url)
        
        print('The site did not provide https proxy, so now your proxy is used')

        return r


def write_csv(data):
    
    with open('videos.csv', 'a') as f:
        
        order = ['name', 'views', 'duration', 'url']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_page_data(response):
    
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['content_html']

    soup = BeautifulSoup(html, 'lxml')

    items = soup.find_all('div', class_='yt-lockup-dismissable')

    for item in items:
        
        i = item.find('div', 'yt-lockup-content')
        
        name = i.find('a').text.strip()
        url = i.find('a').get('href')
        
        views = i.find('li').text.strip()
        views = re.findall(r'\d+', views)       
        views_str = str()
        
        for i in views:
            views_str += i
        
        duration = item.find('span', class_='video-time').text.strip()

               
        data = {'name': name.translate(non_bmp_map),
                'views': views_str,
                'duration': duration,
                'url': url.translate(non_bmp_map)
                }
        
        write_csv(data)


def get_next(response):
    
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['load_more_widget_html']

    soup = BeautifulSoup(html, 'lxml')

    try:
        href = soup.find('button', class_='load-more-button').get('data-uix-load-more-href')
        url = 'https://youtube.com' + href
    except:
        url = ''

    return url


def main():

    #add a channel address here
    url = ' Channel url '
    
    while True:

        response = get_html(url)
        get_page_data(response)

        url = get_next(response)

        if url:
            continue
        else:
            break


if __name__ == '__main__':
    main()
