
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request

import os, bs4
from getpass import getpass
from tqdm import tqdm
import ssl
import time, datetime, re
import pickle

from .data import *
from .config import *

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


def download_images(ID):
    driver = login(DEFAULT_ID, DEFAULT_PW, BASE_URL)
    driver.get(BASE_URL + '/' + ID + '/')
    
    html = driver.page_source
    imgs = bs4.BeautifulSoup(str(html)).select(IMG_CLASS)
    
    for index, img in tqdm(enumerate(imgs)):
        src = img['src'].replace('amp;', '')
        context = ssl._create_unverified_context()
        download = urllib.request.urlopen(src, context=context).read()
        
        with open('/Users/onandon/Downloads/nerf/nerf/static/imgs/' + ID + str(index) + '.jpg', 'wb') as f:
            f.write(download)
        
    driver.quit()
    return None
    
"""
driver = login(DEFAULT_ID, DEFAULT_PW, BASE_URL)
url = BASE_URL + '/' + 'yellow_for_me' + '/'
# driver = webdriver.Chrome(CHROME_DRIVER)
driver.get(url)

html = driver.page_source
img = bs4.BeautifulSoup(str(html)).select(IMG_CLASS)
for i in img:
    if len(img) == 0:
        continue
        
    src = i['src'].replace('amp;', '')
    print(src)
    print()
"""

"""
webelements = driver.find_elements(by=By.CLASS_NAME, value='FFVAD')

for webelement in webelements:
    html = webelement.get_attribute('innerHTML')
    print(str(html))
    print("hello")
    print()
"""

"""
driver = login(DEFAULT_ID, DEFAULT_PW, BASE_URL)

# 프로필 첫 게시물 클릭
first_post = driver.find_element(by=By.CLASS_NAME, value='eLAPa')
first_post.click()

while True:
    try:
        article = ArticleDTO()
        driver = article._init_from_crawling_profile(driver)
        
        print('next pic!')
        print()
        
        next_post = driver.find_element(by=By.CLASS_NAME, value='l8mY4.feth3')
        next_post.click()
    except:
        break

print('END')
"""