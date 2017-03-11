# -*- coding: utf-8 -*-
import requests
import re

class crawler:
    def __init__(self):
        self.session = requests.Session()
        self.referer = None # 用來存放header要用的referer
        self.downloadRootPath = u'D:\嗚流吉他' # 下載影片的根目錄

    def login(self):
        s = None
        return s

    # 取得存放vimeo影片的iframe的連結 (有可能有多個iframe 要改成回傳list)
    def getIframeLinks(self,url):
        '''
        :param url: 傳入要抓取頁面的url
        :return:
        '''
        self.referer = url
        # step1 取得頁面上的vimeo iframe連結
        r = self.session.get(url)
        m = re.search(r'(?P<match>//player.vimeo.com/video/\d*/?[^\"\"]*)', r.text)
        return m.group('match')if m is not None else '抓不到iframe連結'

    def getVideoLink(self,url):
        '''
        :param url: 傳入vimeo iframe的url
        :return:
        '''
        # step2 取得vimeo iframe裡的內容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Referer': self.referer
        }

        r2 = self.session.get('https:' + url, headers=headers)

        # 找出vimeo 影片的下載連結
        m2 = re.search(r'(?P<match>https?://[0-9a-zA-Z-]*.vimeocdn.com/[a-z-\d/]+.mp4[^\"]*)', r2.text)

        return m2.group('match') if m2 is not None else '抓不到vimeo mp4檔'

    def downloadVideo(self,url,path):
        '''
        :param url: 影片下載連結
        :param path: 根目錄後的子目錄跟檔名  例如: 大分類\小分類\xxxx.mp4
        :return:
        '''
        r = self.session.get(url, stream=True)
        print(u'開始下載影片'+path)
        with open(self.downloadRootPath+'\\'+ path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush() commented by recommendation from J.F.Sebastian
        return path

if __name__ =="__main__":
    cw = crawler()
    iflink = cw.getIframeLinks('http://realsound.tw/members/style-step2/')
    videolink = cw.getVideoLink(iflink)
    cw.downloadVideo(videolink,'test.mp4')
    print(videolink)
