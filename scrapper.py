import requests 
from bs4 import BeautifulSoup 

r = requests.get('https://www.failory.com/failures')

soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify()) 