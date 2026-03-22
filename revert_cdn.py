import os
import re

def revert_cdn_to_local():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We need to revert all JSdelivr/Staticaly URLs back to local relative paths
        # From: https://gcore.jsdelivr.net/gh/g2978227503-cloud/portfolio@main/images/...
        # To: images/...
        
        # This regex matches the CDN prefix we added
        pattern = re.compile(r'https://(?:gcore\.jsdelivr\.net/gh|fastly\.jsdelivr\.net/gh|cdn\.staticaly\.com/gh)/g2978227503-cloud/portfolio(?:@|/)main/(images/[^"\']+)')
        
        new_content = pattern.sub(r'\1', content)
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Reverted to local paths in {file}")

if __name__ == "__main__":
    revert_cdn_to_local()
