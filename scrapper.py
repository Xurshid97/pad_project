import requests 
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# r = requests.get('https://www.failory.com/failures')

# soup = BeautifulSoup(r.content, 'html.parser') 
# s = soup.find('div', class_='w-dyn-list') 

# list_of_country_links = s.find_all('a') 

browser = webdriver.Firefox()
browser.get('https://www.failory.com/failures')

def close_pop_up():
    try:
        pop_up_close_button = browser.find_element(By.CLASS_NAME, "popup-icon-close")
        pop_up_close_button.click()
        print('pop up appeared')
    except:
        print("Popup did not appear within the specified time.")


def click_country_button(browser, country_button_class_name):
    try:
        country_button = browser.find_element(By.ID, country_button_class_name)
        country_button.click()
        return browser.current_url
    except:
        close_pop_up()


# enter every country and save their data to a file
url_of_country = click_country_button(browser, 'w-node-c78e2231-b714-552c-3658-765240b39563-a65bf16a')

r = requests.get(url_of_country)
soup = BeautifulSoup(r.content, 'html.parser')

list_of_failed_startups = []

items = soup.find_all(class_="listicle-startup-collection-item")

for item in items:
    h3_tag = item.find('h3', class_='listicle-h3')
    info = {}
    information_of_start_up = ['founder', 'country', 'industry', 'started_in', 'closed_in', '#_of_employees', 'funding_amount', 'cause']
    informations = item.find_all(class_='failed-startup-list-information')
    for i in range(len(informations)):
        if i < len(information_of_start_up):
            info[information_of_start_up[i]] = informations[i].get_text(strip=True)
    each_start_up = {}
    if h3_tag:
        startup_name = h3_tag.get_text(strip=True)
        each_start_up[startup_name] = info
    list_of_failed_startups.append(each_start_up)
print(list_of_failed_startups)

# some mistakes on extracting data, some startups do not have n of employees, also, some has no funding solve it by its name