
from .config import *
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import bs4

class ArticleDTO:
    def __init__(self):
        self.CSS_FEED = {
            'author': AUTHOR_CLASS,
            'author_img': AUTHOR_IMG_CLASS,
            'img': IMG_CLASS,
            'caption': CAPTION_CLASS
        }
        
        self.CSS_PROFILE = {
            'driver_img': PROFILE_POST_IMG_CLASS,
            'driver_img_tag': PROFILE_POST_IMG_CLASS_TAG,
            'driver_single_img': PROFILE_SINGLE_POST_IMG_CLASS,
            'driver_next_pic': PROFILE_NEXT_PIC
        }
        
        self.CSS = {**self.CSS_FEED, **self.CSS_PROFILE}
        
        self.uid = None
        self.author = None
        self.author_photo_url = None
        self.img_urls = []
        self.date = None
        self.caption = None
    
    def _init_from_crawling_data(self, bs4):
        """
        author = bs4.select(self.CSS['author'])
        print(author)
        self.author = author[0].contents[0]
        
        author_img = bs4.select(self.CSS['author_img'])
        self.author_photo_url = author_img[0]['src'].replace('amp;', '')
        """
        
        img_urls = bs4.select(self.CSS['img'])
        for img_url in img_urls:
            self.img_urls.append(img_url['src'].replace('amp:', ''))
        
        """
        try:
            caption = bs4.select(self.CSS['caption'])
            self.caption = caption[2].contents[0]
        except:
            pass
        """
    def _init_from_crawling_profile(self, driver : WebDriver):
        while True:
            try:
                driver.implicitly_wait(3)
        
                for css in [self.CSS['driver_img'], self.CSS['driver_img_tag'], self.CSS['driver_single_img']]:
                    self.img_urls = self._crawl_img_src_in_profile_post(driver, self.img_urls, css)

                next_pic = driver.find_element(by=By.CLASS_NAME, value=self.CSS['driver_next_pic'])
                next_pic.click()
            except:
                break
        
        print(len(self.img_urls))
        
        return driver
    
    def _crawl_img_src_in_profile_post(self, driver : WebDriver, img_src_lst, css):
        try:
            webelement = driver.find_elements(by=By.CLASS_NAME, value=css)
            for web in webelement:
                html = web.get_attribute('innerHTML')
                img = bs4.BeautifulSoup(str(html)).select(self.CSS['img'])
                if len(img) == 0:
                    continue
        
                src = img[0]['src'].replace('amp;', '')
                if src in img_src_lst:
                    continue
                
                img_src_lst.append(src)
        except:
            pass
    
        return img_src_lst
    
    def __repr__(self):
        begin_tag = "=================================================\n\n"
        end_tag = "\n\n================================================="
        head = "<Article data type>\n\n"
        return begin_tag + head + "[author]: {}\n\n[author's photo]: {}\n\n[img]: {}\n\n[capiton]: {}".format(
            self.author, self.author_photo_url, self.img_urls, self.caption
        ) + end_tag


class ProfileDTO:
    def __init__(self):
        pass
    
    def _init_from_crawling_not_login_vr(self, driver):
        pass