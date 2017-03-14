# -*- coding: utf-8 -*-
import re
text="""
<p><iframe src="http://player.vimeo.com/video/70280990" height="405" width="720" allowfullscreen="" frameborder="0"></iframe></p>
<p>&nbsp;</p>

<ul class="bullet-list 1" >
<li style='background-image:url("http://realsound.tw/active-member/wp-content/plugins/optimizePressPlugin/lib/assets/images/bullet_block/32x32/34.png");background-repeat:no-repeat;'>B段</li>
</ul>

<p><iframe src="//player.vimeo.com/video/73197970" height="405" width="720" allowfullscreen="" frameborder="0"></iframe></p>
"""
iframeList = re.findall(r'(?P<match>(?:http:)?//player.vimeo.com/video/\d*/?[^\"\"]*)', text)

for i,url in enumerate(iframeList):
    if url.startswith('/'):
        url='https:'+url
    print(url)