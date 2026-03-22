import os
import re

# GitHub repository information
GITHUB_USER = "g2978227503-cloud"
GITHUB_REPO = "portfolio"
BRANCH = "main"

# Staticaly CDN format
# https://cdn.staticaly.com/gh/user/repo/branch/path/to/file
CDN_PREFIX = f"https://cdn.staticaly.com/gh/{GITHUB_USER}/{GITHUB_REPO}/{BRANCH}/"

def replace_image_paths_in_html():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace src="images/..." or src="./images/..."
        # We need to be careful not to replace already replaced URLs
        # Regex explanation:
        # src=["'](?!http)(?:\.\/)?(images\/[^"']+)["']
        # matches src="images/..." but NOT src="http..."
        
        pattern_img = re.compile(r'src=["\'](?!http)(?:\.\/)?(images\/[^"\']+)["\']')
        
        def replace_match(match):
            img_path = match.group(1)
            # Make sure it's an image or video, though we only want to CDN images mostly. 
            # Staticaly handles images well. For videos, it might have size limits, 
            # but let's try it for all static assets in 'images' folder first.
            if img_path.endswith('.mp4'):
                # Better to keep videos local or use jsdelivr for raw access, 
                # Staticaly is mainly for images/js/css.
                # Let's use fastly.jsdelivr.net for videos
                return f'src="https://fastly.jsdelivr.net/gh/{GITHUB_USER}/{GITHUB_REPO}@{BRANCH}/{img_path}"'
            else:
                return f'src="{CDN_PREFIX}{img_path}"'
        
        new_content = pattern_img.sub(replace_match, content)
        
        # Also handle data-preview="images/..." if any (though you used unsplash for those)
        pattern_data = re.compile(r'data-preview=["\'](?!http)(?:\.\/)?(images\/[^"\']+)["\']')
        new_content = pattern_data.sub(replace_match, new_content)
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated image paths in {file}")

if __name__ == "__main__":
    replace_image_paths_in_html()
    print("Done replacing image paths with CDN links.")
