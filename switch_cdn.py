import os
import re

def switch_cdn_to_jsdelivr():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace Staticaly with jsdelivr gcore node
        # Old: https://cdn.staticaly.com/gh/g2978227503-cloud/portfolio/main/images/
        # New: https://gcore.jsdelivr.net/gh/g2978227503-cloud/portfolio@main/images/
        
        new_content = content.replace(
            'https://cdn.staticaly.com/gh/g2978227503-cloud/portfolio/main/',
            'https://gcore.jsdelivr.net/gh/g2978227503-cloud/portfolio@main/'
        )
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated CDN to jsDelivr in {file}")

if __name__ == "__main__":
    switch_cdn_to_jsdelivr()
