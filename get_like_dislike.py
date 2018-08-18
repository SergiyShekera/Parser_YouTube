import requests
import re

from bs4 import BeautifulSoup


def get_like_dislike(url):
   
    response = requests.get(url)
    
    html = response.text

    soup = BeautifulSoup(html, 'lxml')

    data = soup.find('div', id='watch8-sentiment-actions')
    data = data.find('span', class_='like-button-renderer')

    like = data.find('button', 'like-button-renderer-like-button').text.strip()
    dislike = data.find('button', 'like-button-renderer-dislike-button').text.strip()
    
    like = re.findall(r'\d+', like)       
    like_str = str()
    
    for i in like:
        like_str += i

    dislike = re.findall(r'\d+', dislike)       
    dislike_str = str()
    
    for i in dislike:
        dislike_str += i

    ld = {'like': like_str, 'dislike': dislike_str}
    
        
    return ld


