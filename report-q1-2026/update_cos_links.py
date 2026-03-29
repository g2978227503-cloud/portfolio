import re
import os
import urllib.parse

file_path = '/Users/miki/Documents/NETEASE/goofy-portfolio/trial/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 把之前错误的 images/trial 替换回直接的 trial/
old_prefix = "https://goofy-portfolio-1342690925.cos.ap-guangzhou.myqcloud.com/images/trial/"
new_prefix = "https://goofy-portfolio-1342690925.cos.ap-guangzhou.myqcloud.com/trial/"

content = content.replace(old_prefix, new_prefix)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed COS prefix")
