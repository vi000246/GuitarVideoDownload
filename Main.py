# -*- coding: utf-8 -*-
import csv
import pandas as pd
from tempfile import NamedTemporaryFile
import shutil,sys
from crawler import crawler
import logging
logging.basicConfig(filename='event.log',level=logging.DEBUG)
logging.info('========開始執行程式============')

filename = 'url.csv'
# 登入吉他網
cw = crawler()

tempfile = NamedTemporaryFile(delete=False)
# 開啟CSV
with open(filename, 'rb') as csvFile, tempfile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='"')
    writer = csv.writer(tempfile, delimiter=',', quotechar='"')
    next(reader, None)  # skip the headers
    # 逐行讀取CSV內容
    for row in reader:
        if row[4] == 'n':
            # print('檔名:'+str(row[0])+' 目錄:' + str(row[2])+str(row[1]))
            videoList = cw.getVideoLinkList(str(row[3]))
            for i, url in enumerate(videoList):
                cw.downloadVideo(str(row[0]), url)

            # 如果成功下載 將isDownload改為y
            row[4] = 'y'
            # 將每行寫入temp csv
            writer.writerow(row)
            logging.info('目前進度 '+str(row[0])+':'+str(row[1])+':'+str(row[2]))

# 將temp csv覆蓋原csv
shutil.move(tempfile.name, filename)


