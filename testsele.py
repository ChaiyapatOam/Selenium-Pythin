from selenium import webdriver
from bs4 import BeautifulSoup as soup

driver = webdriver.Chrome(r'C:\Users\ADMIN\Desktop\Selenium\chromedriver.exe')

url = 'https://myanimelist.net/topanime.php'

driver.get(url)