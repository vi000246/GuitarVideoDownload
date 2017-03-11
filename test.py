# -*- coding: utf-8 -*-
import requests
import re

# step1 取得頁面上的vimeo iframe連結
s = requests.Session()
url = 'http://realsound.tw/members/style-step2/'
r = s.get(url)
m = re.search(r'(?P<match>//player.vimeo.com/video/\d*/?[^\"\"]*)',r.text)

# step2 取得vimeo iframe裡的內容
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': url
}

r2 = s.get('https:'+m.group('match'),headers=headers)

# 找出vimeo 影片的下載連結
m2 = re.search(r'(?P<match>https?://[0-9a-zA-Z-]*.vimeocdn.com/[a-z-\d/]+.mp4[^\"]*)',r2.text)

print(m2.group('match'))