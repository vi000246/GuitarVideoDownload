import re
text = """
<p><iframe src="http://player.vimeo.com/video/72791860" width="720" height="405" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></p>

<ul class="bullet-list 1" >
<li style='background-image:url("http://realsound.tw/active-member/wp-content/plugins/optimizePressPlugin/lib/assets/images/bullet_block/32x32/34.png");background-repeat:no-repeat;'>前奏1</li>
</ul>

<p><iframe src="https://player.vimeo.com/video/126774675" width="720" height="405" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></p>
<p>&nbsp;</p>

<ul class="bullet-list 1" >
<li style='background-image:url("http://realsound.tw/active-member/wp-content/plugins/optimizePressPlugin/lib/assets/images/bullet_block/32x32/34.png");background-repeat:no-repeat;'>前奏2</li>
</ul>

<p><iframe src="https://player.vimeo.com/video/126776097" width="720" height="405" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></p>
<p>&nbsp;</p>

<ul class="bullet-list 1" >
<li style='background-image:url("http://realsound.tw/active-member/wp-content/plugins/optimizePressPlugin/lib/assets/images/bullet_block/32x32/34.png");background-repeat:no-repeat;'>主歌1</li>
</ul>

<p><iframe src="https://player.vimeo.com/video/126778643" width="720" height="405" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></p>
<p>&nbsp;</p>

<ul class="bullet-list 1" >
<li style='background-image:url("http://realsound.tw/active-member/wp-content/plugins/optimizePressPlugin/lib/assets/images/bullet_block/32x32/34.png");background-repeat:no-repeat;'>主歌2</li>
</ul>

<p><iframe src="https://player.vimeo.com/video/126781378" width="720" height="405" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></p>
<p>&nbsp;</p>

"""
iframeList = re.findall(r'(?P<match>//player.vimeo.com/video/\d*/?[^\"\"]*)', text)