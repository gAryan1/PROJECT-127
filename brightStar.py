from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/w/index.php?title=List_of_brightest_stars_and_other_record_stars&oldid=945771782"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)
scrap_data = []

def scrape():
        
    # BeautifulSoup Object     
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs = {"class", "wikitable"})

    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all("tr")
    
    for row in table_rows:
        table_cols = row.find_all('td')
        #print(table_cols)
        temp_list = []
        

        for cols_data in table_cols:
           # print(cols_data.text)
            data = cols_data.text.strip()
           # print(data)
            temp_list.append(data)
        scrap_data.append(temp_list)



scrape()

stars_data = []

for i in range(0,len(scrap_data)):

    star_names = scrap_data[i][1]
    distance = scrap_data[i][3]
    mass = scrap_data[i][5]
    radius = scrap_data[i][6]
    lum = scrap_data[i][7]

    required_data = [star_names, distance, mass, radius, lum]
    stars_data.append(required_data)

headers = ['star_names', 'distance', 'mass', 'radius', 'luminosity']
star_df = pd.DataFrame(stars_data, columns=headers)
star_df.to_csv('scrapedata.csv', index = True, index_label='id')