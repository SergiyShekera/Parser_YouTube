import requests
import csv
import sys
import re

from multiprocessing import Pool
from bs4 import BeautifulSoup
from Proxy import get_proxy
from get_like import get_like
from get_dislike import get_dislike 
from write_database import write_database


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

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


def write_csv(data):
    
    with open('videos.csv', 'a') as f:
        
        order = ['name', 'views', 'like', 'dislike','duration', 'url']
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

        url = 'https://youtube.com' + url
        
        like = get_like(url)
        dislike = get_dislike(url)
        
        duration = item.find('span', class_='video-time').text.strip()

               
        data = {
                'name': name.translate(non_bmp_map),
                'views': views_str,
                'like': like,
                'dislike': dislike,
                'duration': duration,
                'url': url
                }
        
        #write_csv(data)
        #print(data)
        write_database(data)


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

def make_all(url):   
    response = get_html(url)
    get_page_data(response)
    
def main():

    #add a channel address here
    url = ' Channel url '
 
    urls = []
    
    while True:
        
        response = get_html(url)
        
        urls.append(url)
        
        url = get_next(response)

        if url:
            continue
        else:
            break

    with Pool(15) as p:
        p.map(make_all, urls)
        
if __name__ == '__main__':
    
    main()
    
    print('Parsing finished')
    q = input('press Enter to exit')
