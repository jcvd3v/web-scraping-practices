from bs4 import BeautifulSoup
import requests
import pandas as pd

# Creating Scraper Object
class Scraper:
    def __init__(self, delay=1, timeout=10, headers=None):
        self.delay = delay
        self.timeout = timeout
        self.session = requests.Session()
        if headers: 
            self.session.headers.update(headers)
    def get(self, url):
        r = self.session.get(url, timeout=self.timeout)
        soup=BeautifulSoup(r.text, 'html.parser')
        return soup


default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',  # Identify the app to simulate a browser
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9',
        'Accept-Language':'en-US,en;q=0.9'}

url = 'https://loteriadehoy.com/loterias/resultados/'

scraper = Scraper(delay=2, timeout=20, headers=default_headers)

with open('page.html', 'w', encoding="utf-8") as f:
    f.write(str(scraper.get(url)))