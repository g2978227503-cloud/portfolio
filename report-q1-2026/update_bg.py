file_path = '/Users/miki/Documents/NETEASE/goofy-portfolio/trial/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the extra spaces that were breaking the background parsing in CSS
# The issue might be URL encoding inside the CSS url() function. Let's try raw chinese characters since HTML can handle it.
content = content.replace("url('https://goofy-portfolio-1342690925.cos.ap-guangzhou.myqcloud.com/trial/%E7%94%BB%E6%9D%BF.png')", "url('https://goofy-portfolio-1342690925.cos.ap-guangzhou.myqcloud.com/trial/画板.png')")
content = content.replace("url('https://goofy-portfolio-1342690925.cos.ap-guangzhou.myqcloud.com/trial/%E7%94%BB%E6%9D%BF2.png')", "url('https://goofy-portfolio-1342690925.cos.ap-guangzhou.myqcloud.com/trial/画板2.png')")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
