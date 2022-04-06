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
## Run the Django!!
`nerf/nerf/views.py`에서 `download_images()` 함수의 인자로 크롤링하고 싶은 유저의 아이디를 넣어주세요. (디폴트로 'yellow_for_me')가 들어가 있음.

```python
...

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        
        # input에 크롤링하고 싶은 유저의 아이디를 입력
        download_images('yellow_for_me')
        return {}
```

터미널 창에 `python3 manage.py runserver 0:8000` 커맨드를 입력하면 장고내 개발용 서버가 열립니다.

이후 `http//127.0.0.1:8000/download` url로 접속하면 SUCCESS!라는 문구와 함께, 여러분의 컴퓨터에 있는 크롬 창이 저절로 열리면서 자동으로 인스타에 nerf.lab 계정으로 로그인 한 뒤, 
크롤링을 시작합니다. (크롤링 도중 마우스로 다른 곳을 클릭하지 말것)

`nerf/static/imgs/` 폴더 내, 입력한 유저 프로필에 있는 사진 최대 12장이 다운로드 되어질 것입니다.
이때,
* 유저가 공개 아이디여야 합니다. (비공개면 크롤링 안됨)
* 프로필에 올라와있는 게시물이 12개 이상이면 12개만 크롤링합니다.
* 게시물이 12개 이하이면 게시물 개수만큼 크롤링합니다.
* 인스타 문제로 가끔 로그인 하는 과정에서 네트워크 오류가 뜰 수 있는데, 서버를 끄고 다시 시작하면 잘 됨.
* 크롤링을 너무 자주 시도하면 nerf.lab 계정 로그인이 막힐 수 있음 > 하루 뒤에 풀림
