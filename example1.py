# Import Libraries
from bs4 import BeautifulSoup
import requests

# set url
url = "https://quotes.toscrape.com/"

# request the url
response = requests.get(url)

# Parse
soup=BeautifulSoup(response.text, 'html.parser')

# find 'div' class_='quote'
quotes=soup.find_all('div', class_='quote') # quotes list

# Get author and quote.
for quote in quotes:
    text = quote.find('span', class_='text') 
    author = quote.find('small', class_='author')
    print (f"Quote: {text.text}")
    print (f"Author: {author.text}\n")

# Write in a .txt file
with open("quotes.txt", "w", encoding="utf-8") as f:
    for quote in quotes:
        text = quote.find('span', class_='text') 
        author = quote.find('small', class_='author')
        f.write(f'Quote: {text.text}\nAuthor:{author.text}\n\n')