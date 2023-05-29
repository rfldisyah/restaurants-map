# INI CONTOH MENGGUNAKAN SELENIUM
# Kalau Selenium memerlukan instalasi WebDriver untuk browser yang digunakan, seperti chromedriver untuk Chrome
# Trus waktu eksekusi Selenium memerlukan waktu lebih lama karena memuat halaman web menggunakan browser web dan melakukan interaksi.

from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver')
url = "https://www.spacex.com/launches/"
driver.get(url)
sleep(5)

sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(10)

req = driver.page_source
driver.quit()
soup = BeautifulSoup(req, 'html.parser')

items = soup.find_all('div', {'class': ['item']})
for item in items:
    date = item.select_one('.date')
    label = item.select_one('.label')

    print(date)
    print(label)






# INI CONTOH MENGGUNAKAN REQUEST
# Kalau Requests hanya memerlukan instalasi modul python requests saja
# Trus waktu eksekusi Requests umumnya lebih cepat karena mengambil data secara langsung dari server.

import requests
from bs4 import BeautifulSoup

url = "https://www.spacex.com/launches/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

req = data.text
soup = BeautifulSoup(req, 'html.parser')

items = soup.find_all('div', {'class': ['item']})
for item in items:
    date = item.select_one('.date')
    label = item.select_one('.label')
    
    if not date:
        continue
    date = date.text.strip()
    label = label.text.strip()
    
    print(date, ' ', label, ' ')


