import requests

url = 'https://httpbin.org/'

default_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',  # Identify the app to simulate a browser
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9',
            'Accept-Language':'en-US,en;q=0.9'
        }

r = requests.get(url, default_headers)