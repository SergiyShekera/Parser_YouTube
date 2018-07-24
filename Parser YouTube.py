import requests
import csv

from bs4 import BeautifulSoup



def get_html(url):
    r = requests.get(url)
    return r

def write_csv(data):
    with open('videos.csv', 'a') as f:
        order = ['name', 'duration', 'url']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_page_data(response):
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['content_html']

    soup = BeautifulSoup(html, 'lxml')

    items = soup.find_all('h3', class_='yt-lockup-title')

    for item in items:
        name = item.find('a').text.strip()
        url = item.find('a').get('href')
        duration = item.find('span', class_='accessible-description').text.strip()

        data = {'name': name, 'duration': duration, 'url': url}
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
