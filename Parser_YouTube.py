import requests
import sys
import re

from multiprocessing import Pool
from bs4 import BeautifulSoup
from get_html import get_html
from get_next import get_next
from get_like_dislike import get_like_dislike
from write_csv import write_csv
from write_database import write_database


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


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
        
        ld = get_like_dislike(url)
        
        like = ld['like']
        dislike = ld['dislike']
        
        duration = item.find('span', class_='video-time').text.strip()

               
        data = {
                'name': name.translate(non_bmp_map),
                'views': views_str,
                'like': like,
                'dislike': dislike,
                'duration': duration,
                'url': url
                }
        
        write_csv(data)
        print(data)
        #write_database(data)



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
