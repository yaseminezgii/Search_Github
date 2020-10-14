from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import pandas as pd

def current_page():
    browser = webdriver.Chrome()
    keyword = "deneme"
    browser.get('https://github.com/search')
    elem = browser.find_element_by_name('q')
    elem.send_keys(keyword + Keys.RETURN)
    return browser.current_url

url = current_page()
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi,"html.parser")

linkler= soup.find_all("a", {"class":"v-align-middle"})
tarih= soup.find_all("relative-time", {"class":"no-wrap"})

records = []
for LINK, DATE in zip(linkler, tarih):
    LINK = LINK.text
    DATE = DATE.text

    LINK = LINK.strip()
    LINK = LINK.replace("\n", "")

    DATE = DATE.strip()
    DATE = DATE.replace("\n", "")

    records.append((LINK, DATE))

df = pd.DataFrame(records, columns=['LINK', 'DATE'])
print (df)

"""
writer = pd.ExcelWriter('Github_search.xlsx', engine='xlsxwriter')
df.to_excel(writer,  'results')
writer.save()

browser.quit()
"""
