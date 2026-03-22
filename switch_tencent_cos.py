import os
import re

def switch_to_tencent_cos():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # 腾讯云 COS 域名
    cos_domain = "https://goofy-portfolio-1342690925.cos.ap-guangzhou.myqcloud.com"
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. 替换标准的 src="images/..."
        # Regex explanation:
        # src=["'](?!http)(?:\.\/)?(images\/[^"']+)["']
        pattern_src = re.compile(r'src=["\'](?!http)(?:\.\/)?(images\/[^"\']+)["\']')
        
        # 2. 替换 data-preview="images/..."
        pattern_data = re.compile(r'data-preview=["\'](?!http)(?:\.\/)?(images\/[^"\']+)["\']')
        
        def replace_match(match):
            img_path = match.group(1)
            return f'src="{cos_domain}/{img_path}"'
            
        def replace_match_data(match):
            img_path = match.group(1)
            return f'data-preview="{cos_domain}/{img_path}"'
        
        new_content = pattern_src.sub(replace_match, content)
        new_content = pattern_data.sub(replace_match_data, new_content)
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated paths to Tencent COS in {file}")

if __name__ == "__main__":
    switch_to_tencent_cos()
