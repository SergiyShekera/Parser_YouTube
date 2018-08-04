import requests
import re

from bs4 import BeautifulSoup


def get_dislike(url):

    response = requests.get(url)
    
    html = response.text

    soup = BeautifulSoup(html, 'lxml')

    data = soup.find('div', id='watch8-sentiment-actions')
    data = data.find('span', class_='like-button-renderer')

    dislike = data.find('button', 'like-button-renderer-dislike-button').text.strip()
    
    dislike = re.findall(r'\d+', dislike)       
    dislike_str = str()
    
    for i in dislike:
        dislike_str += i

        
    return dislike_str

