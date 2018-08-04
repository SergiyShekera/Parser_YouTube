import requests
import re

from bs4 import BeautifulSoup


def get_like(url):
   
    response = requests.get(url)
    
    html = response.text

    soup = BeautifulSoup(html, 'lxml')

    data = soup.find('div', id='watch8-sentiment-actions')
    data = data.find('span', class_='like-button-renderer')

    like = data.find('button', 'like-button-renderer-like-button').text.strip()
    
    like = re.findall(r'\d+', like)       
    like_str = str()
    
    for i in like:
        like_str += i
        
    return like_str
