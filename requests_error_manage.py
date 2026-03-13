import requests
url = 'https://httpbin.org/status/404'
r = requests.get(url)
if r.status_code != 200:
    print(f'HTTP ERROR: {r.status_code}')

try:
    re = requests.get(url)
    re.raise_for_status()
except requests.exceptions.HTTPError as e:
     print(f'HTTP ERROR: {e}')