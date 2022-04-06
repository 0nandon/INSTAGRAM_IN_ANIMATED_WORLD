# INSTAGRAM_IN_ANIMATED_WORLD

## Versions

파이썬 가상환경 버전 : 3.7.2

`pip install -r requirements.txt` 으로 나머지 라이브러리 버전 맞춰서 설치하기!

## Check list

### 크롬 버전 확인하기!
컴퓨터에 반드시 크롬 버전 `100`이 깔려 있어야 합니다. 버전이 `100`이 아니면 크롤링이 안됨.

### 아래 파일의 인자들을 자신의 컴퓨터에 바꿔주세요.

`/nerf/crawl/config.py`에서 `'nerf/crawl/chromedriver'`의 절대 경로를 복사하여 아래 코드의 `CHROME_DRIVER`에 넣어주세요.
```python
...

# css class for crawling in profile page
PROFILE_POST_IMG_CLASS = 'eLAPa.RzuR0'
PROFILE_POST_IMG_CLASS_TAG = 'eLAPa.vF75o'
PROFILE_SINGLE_POST_IMG_CLASS = 'eLAPa.kPFhm'
PROFILE_NEXT_PIC = 'coreSpriteRightChevron'

CHROME_DRIVER = r"/Users/onandon/Downloads/nerf/nerf/crawl/chromedriver" # 여기에 자신의 컴퓨터에 맞는 경로를 넣어주기!
```
<br>
`/nerf/crawl/crawl_profile.py`에서 `'nerf/static/imgs'` 폴더의 절대 경로를 복사하여 open()함수에 넣어주기. 주석 참고!
```python
...

def download_images(ID):
    driver = login(DEFAULT_ID, DEFAULT_PW, BASE_URL)
    driver.get(BASE_URL + '/' + ID + '/')
    
    html = driver.page_source
    imgs = bs4.BeautifulSoup(str(html)).select(IMG_CLASS)
    
    for index, img in tqdm(enumerate(imgs)):
        src = img['src'].replace('amp;', '')
        context = ssl._create_unverified_context()
        download = urllib.request.urlopen(src, context=context).read()
        
        # 아래 open 함수에 '/Users/onandon/Downloads/nerf/nerf/static/imgs/'부분에 자신의 컴퓨터에 맞는 경로 넣어주기
        with open('/Users/onandon/Downloads/nerf/nerf/static/imgs/' + ID + str(index) + '.jpg', 'wb') as f:
            f.write(download)
        
    driver.quit()
    return None
```
