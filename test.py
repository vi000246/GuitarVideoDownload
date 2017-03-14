# -*- coding: utf-8 -*-
import requests
import re
import os

dir = '初級演奏'
# dir = '樂理完全解密'
path = u'D:\嗚流吉他' +'\\'+ dir.decode('utf-8')
num = []
for root, dirs, files in os.walk(path):
    inputName = 'Pachelbel【卡農】'
    # inputName = '掛留四和弦 suspended fourth'
    indices = [i for i, x in enumerate(files) if x.startswith(inputName.decode('utf-8'))]
    num.append(len(indices))
print(max(num)+1)