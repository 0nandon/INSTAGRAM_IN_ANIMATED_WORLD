# INSTAGRAM_IN_ANIMATED_WORLD

## Versions

파이썬 가상환경 버전 : 3.7.2

`pip install -r requirements.txt` 으로 나머지 라이브러리 버전 맞춰서 설치하기!

## Check list

### 크롬 버전 확인하기!
컴퓨터에 반드시 크롬 버전 `100`이 깔려 있어야 합니다. 버전이 `100`이 아니면 크롤링이 안됨.

### 아래 파일의 인자들을 자신의 컴퓨터에 바꿔주세요.

/nerf/crawl/config.py에서 'nerf/crawl/chromedriver'의 절대 경로를 복사하여 아래 코드의 `CHROME_DRIVER`에 넣어주세요.
```python
...

# css class for crawling in profile page
PROFILE_POST_IMG_CLASS = 'eLAPa.RzuR0'
PROFILE_POST_IMG_CLASS_TAG = 'eLAPa.vF75o'
PROFILE_SINGLE_POST_IMG_CLASS = 'eLAPa.kPFhm'
PROFILE_NEXT_PIC = 'coreSpriteRightChevron'

CHROME_DRIVER = r"/Users/onandon/Downloads/nerf/nerf/crawl/chromedriver" # 여기에 자신의 컴퓨터에 맞는 경로를 넣어주기!
```

