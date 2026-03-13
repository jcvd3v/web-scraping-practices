from bs4 import BeautifulSoup
import requests

# Creating Scraper Object
class Scraper:
    def __init__(self, delay=1, timeout=10, headers=None):
        self.delay = delay
        self.timeout = timeout
        self_session = requests.Session()

        default_headers = {
            'User-Agent': 'Scraper/1.0'
        }
        pass