# -*- coding: utf-8 -*-
import requests
import re
import sys

class crawler:
    def __init__(self):
        self.session = requests.Session()
        self.downloadRootPath = u'D:\嗚流吉他' # 下載影片的根目錄

    def login(self):
        s = None
        return s

    # 取得存放vimeo影片的iframe的連結 (有可能有多個iframe 要改成回傳list)
    def getVideoLinkList(self,url):
        '''
        :param url: 傳入要抓取頁面的url
        :return:回傳所有的影片下載連結的list
        '''
        # step1 取得頁面上的vimeo iframe連結
        r = self.session.get(url)
        iframeList = re.findall(r'(?P<match>//player.vimeo.com/video/\d*/?[^\"\"]*)', r.text)
        if iframeList is None:
            raise '找不到vimeo的iframe'
        # step2 loop list裡的iframe url 取得影片連結
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Referer': url
        }
        videoLinkList = []
        for i,url in enumerate(iframeList):
            r2 = self.session.get('https:' + url, headers=headers)

            # 找出vimeo 影片的下載連結
            m2 = re.findall(r'(?P<match>https?://[0-9a-zA-Z-]*.vimeocdn.com/[a-z-\d/]+.mp4[^\"]*)', r2.text)
            if m2 is None:
                raise '找不到vimeo影片的下載連結'
            videoLinkList = videoLinkList + m2

        return videoLinkList

    def downloadVideo(self,url,path):
        r = self.session.get(url, stream=True)
        total_length = r.headers.get('content-length')

        print(u'開始下載影片'+path)
        with open(self.downloadRootPath+'\\'+ path, 'wb') as f:
            if total_length is None:  # no content length header
                f.write(r.content)
            else:
                dl = 0
                total_length = int(total_length)
                for chunk in r.iter_content(chunk_size=1024):
                    dl += len(chunk)
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        done = int(50 * dl / total_length)
                        # progress bar
                        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                        sys.stdout.flush()
        return path

if __name__ =="__main__":
    cw = crawler()
    videoList = cw.getVideoLinkList('http://realsound.tw/members/style-step2/')
    for i,url in enumerate(videoList):
        cw.downloadVideo(url,'test.mp4')

