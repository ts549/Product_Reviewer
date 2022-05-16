import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class Parser():

    def __init__(self, url):
        sects = urlparse(url)
        self.scheme = sects[0]
        self.netloc = sects[1]
        self.path = sects[2]
        self.hostname = self.scheme + '://' + self.netloc

    def get_page(self):
        url = self.hostname + self.path
        params = {'url': url, 'wait': 2}
        page = requests.get('http://localhost:8050/render.html', params=params)

        return page

    def get_reviews(self, page):
        soup = BeautifulSoup(page.text, 'html.parser')
        reviews = soup.find_all('div', {'data-hook': 'review'})
        return reviews

    def get_next_page(self, page):
        soup = BeautifulSoup(page.text, 'html.parser')
        ref = soup.find('li', {'class': 'a-last'})


        if (ref.get('class')[0] != 'a-last'):
            return None

        return ref

    def set_path(self, path):
        self.path = path

    def print_details(self):
        print(self.scheme)
        print(self.netloc)
        print(self.hostname)
        print(self.path)