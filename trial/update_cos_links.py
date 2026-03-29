import re
import os

file_path = '/Users/miki/Documents/NETEASE/goofy-portfolio/trial/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

images = [
    "截屏2026-03-28 16.45.47.png",
    "截屏2026-03-28 16.45.26.png",
    "截屏2026-03-28 16.52.40.png",
    "sss.png",
    "首页@1x.png",
    "引导页-回流玩家@1x.png",
    "容器 94@1x.png",
    "地图@1x.png",
    "Clipboard - 2026-01-19 16.55.26.png"
]

import urllib.parse

cos_prefix = "https://goofy-portfolio-1342690925.cos.ap-guangzhou.myqcloud.com/images/trial/"

for img in images:
    # encode the img filename since it has chinese characters and spaces
    encoded_img = urllib.parse.quote(img)
    content = content.replace(f'src="{img}"', f'src="{cos_prefix}{encoded_img}"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
