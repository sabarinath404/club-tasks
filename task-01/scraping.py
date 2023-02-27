import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://www.worldometers.info/coronavirus/#countries'
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
Tsoup = BeautifulSoup(response.content, 'div.label-counter')
# Csoup = BeautifulSoup(response.content, 'a.mt_a')

# Csoup = Csoup.find_all('a', class_='mt_a')
# name=Csoup[0].text
# print(name)

# Extract the title of the website
title = Tsoup.title.string

# Print the title
print(title)