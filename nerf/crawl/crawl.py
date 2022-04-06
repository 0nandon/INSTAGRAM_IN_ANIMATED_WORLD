from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, bs4
from getpass import getpass
import time, datetime, re
import pickle

from data import *
from config import *

PATH = os.path.dirname(__file__)

def login(ID, PW, url):
    """
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    """
    
    driver = webdriver.Chrome(CHROME_DRIVER)
    driver.get(url)
    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "username")))
    username.send_keys(ID)
    password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "password")))
    password.send_keys(PW)
    password.send_keys(Keys.ENTER)
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//button[text()="나중에 하기"]/..'))).click()
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CLASS_NAME, "HoLwm"))).click()

    return driver

driver = login(DEFAULT_ID, DEFAULT_PW, BASE_URL)
html = driver.page_source

"""
with open(os.path.join(PATH, 'crawling.pickle'), 'wb') as f:
    pickle.dump(html, f)

with open(os.path.join(PATH, 'crawling.pickle'), 'rb') as f:
    html = pickle.load(f)
"""

soup = bs4.BeautifulSoup(html)
articles_html = soup.select(ARTICLE_CLASS)

articles = []
for article_html in articles_html:
 
    if IMG_CLASS[1:] not in str(article_html):
        continue
  
    article_soup = bs4.BeautifulSoup(str(article_html))

    article = ArticleDTO()
    article._init_from_crawling_data(article_soup)
    articles.append(article)
    
    print(article)
    print()

driver.close()



