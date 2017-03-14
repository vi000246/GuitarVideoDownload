# -*- coding: utf-8 -*-
import requests
import re

r = requests.get('http://realsound.tw/active-member/center/member-login/')
print(r.text)

iframeList = re.search(r'name=\"_wpnonce\" value=\"(?P<wpnonce>\w*)\"', r.text)

print(iframeList.group('wpnonce'))
