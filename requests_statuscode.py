import requests

url = "https://quotes.toscrape.com/"
r = requests.get(url)

print("Response Code:")
print(r.status_code)
