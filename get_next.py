from bs4 import BeautifulSoup


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
