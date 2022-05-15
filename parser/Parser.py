import requests
from bs4 import BeautifulSoup
import pickle

class Parser(object):

    @staticmethod
    def getHTML(url):
        params = {'url': url, 'wait': 2}
        page = requests.get('http://localhost:8050/render.html', params=params)

        return page.text