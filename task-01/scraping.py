import requests
import csv
from bs4 import BeautifulSoup

 

file = open("myfile.csv", "w")

url = 'https://www.worldometers.info/coronavirus/#countries'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'id': 'main_table_countries_today'})


rows = table.tbody.find_all('tr')
data = []


for row in rows:
    cols = row.find_all('td')
    if len(cols) > 1 and not cols[0].text.strip().startswith(('World','North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania')):
        country = cols[1].text.strip()
        cases = cols[2].text.strip().replace(',', '')
        deaths = cols[4].text.strip().replace(',', '')
        recoveries = cols[6].text.strip().replace(',', '')
        data.append([country, cases, deaths, recoveries])



print('Top 10 countries with the most COVID-19 cases:--')
k=0

print("No.   -country   no. of cases  -no of deaths  -no of recoveries")
for i in range(18):
       
       if (i>=8):
 
         print(f'{k+1}. {data[i][0]} - {data[i][1]} , {data[i][2]} , {data[i][3]} ')
         file.write(f'{k+1}. ;{data[i][0]} ;{data[i][1]} ; {data[i][2]} ; {data[i][3]} \n')
         k=k+1

