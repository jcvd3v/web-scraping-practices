import requests
url = 'https://httpbin.org/delay/10'

try:
    r = requests.get(url, timeout=2) # ReadingTimeOut
except requests.exceptions.Timeout as e:
    print(e)