import requests 
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

browser = webdriver.Firefox()
browser.get('https://www.failory.com/failures')

def get_data_from_country_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    list_of_failed_startups = []
    list_of_main_data = soup.find_all(class_="listicle-list")
    # get listicle-list-item of each list_of_main_data
    for main_data in list_of_main_data:
        listicle_list_items = main_data.find_all(class_="listicle-list-item")
        one_failed_startup = []
        for listicle_list_item in listicle_list_items:
            # get first listicle-list-category and failed-startup-list-information, make a key value pairs, and append to list_of_failed_startups
            category = listicle_list_item.find(class_="listicle-list-category")
            information = listicle_list_item.find(class_="failed-startup-list-information")
            if category and information:
                one_failed_startup.append({category.get_text(strip=True): information.get_text(strip=True)})
        list_of_failed_startups.append(one_failed_startup)
    return list_of_failed_startups

def get_data(browser):
    # get 3rd main-page-container class from a list of same classes
    main_page_container = browser.find_elements(By.CLASS_NAME, "main-page-container")[2]
    # get all a tags href from that main-page-container
    urls_of_countries = [country_link.get_attribute('href') for country_link in main_page_container.find_elements(By.TAG_NAME, "a")]

    final_data = []
    # for each country, get the data from the country page
    for url_of_country in urls_of_countries:
        final_data.append(get_data_from_country_page(url_of_country))
    return final_data

final_data_failed_startups = get_data(browser)

# convert final_data to json
with open('./unstructured_scrapping/failed_starts/final_data_failed_startups.json', 'w') as f:
    json.dump(final_data_failed_startups, f)




# sucessfull startups
def get_data_from_country_page_success(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    list_of_successfull_startups = []
    # find by id failed-startup-text
    list_of_main_data = soup.find_all(id="failed-startup-text")
    # get listicle-list-item of each list_of_main_data
    for main_data in list_of_main_data:
        listicle_list_items = main_data.find_all("ul")
        for list_item in listicle_list_items:
            list_of_itmes = list_item.find_all("li")
            one_successfull_startup = []
            for item in list_of_itmes:
                print(item.string)
                item_data = item.string.split(":") if ':' in item.string else ['no key', 'no value']
                key = item_data[0].strip()
                value = item_data[1].strip()
                one_successfull_startup.append({key: value})
            print(one_successfull_startup)
            list_of_successfull_startups.append(one_successfull_startup)
    return list_of_successfull_startups


def get_data_success(browser):
    # get 3rd main-page-container class from a list of same classes
    main_page_container = browser.find_elements(By.CLASS_NAME, "main-page-container")[1]
    # get all a tags href from that main-page-container
    urls_of_countries = [country_link.get_attribute('href') for country_link in main_page_container.find_elements(By.TAG_NAME, "a")]

    final_data = []
    # for each country, get the data from the country page
    for url_of_country in urls_of_countries:
        final_data.append(get_data_from_country_page_success(url_of_country))
    return final_data

browser.get('https://www.failory.com/startups')
final_data_successfull_startups = get_data_success(browser)
with open('./unstructured_scrapping/success_start/final_data_successfull_startups.json', 'w') as f:
    json.dump(final_data_successfull_startups, f)
# browser.quit()