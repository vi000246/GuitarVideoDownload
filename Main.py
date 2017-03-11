# -*- coding: utf-8 -*-
import csv
import pandas as pd
from tempfile import NamedTemporaryFile
import shutil


filename = 'url.csv'


tempfile = NamedTemporaryFile(delete=False)
# 開啟CSV
with open(filename, 'rb') as csvFile, tempfile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='"')
    writer = csv.writer(tempfile, delimiter=',', quotechar='"')
    # 逐行讀取CSV內容
    for row in reader:
        # 如果成功下載 將isDownload改為y
        row[4] = 'y'
        # 將每行寫入temp csv
        writer.writerow(row)

# 將temp csv覆蓋原csv
shutil.move(tempfile.name, filename)

