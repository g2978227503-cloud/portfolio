import os
import re
import glob

# First, let's update the image references in all HTML files
def update_html_references():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We need to replace .png, .jpg, .jpeg with .webp in the CDN URLs and local URLs
        # Example: images/profile.jpg -> images/profile.webp
        
        # Function to replace extensions if the target webp file actually exists
        # But since we just converted everything and deleted originals, we should just replace the extensions
        # in the HTML strings for all standard image types
        
        # Replace in standard src attributes
        new_content = re.sub(r'(images/[^"\']+)\.(png|jpg|jpeg)', r'\1.webp', content, flags=re.IGNORECASE)
        
        # Replace in CDN URLs
        new_content = re.sub(r'(portfolio/main/images/[^"\']+)\.(png|jpg|jpeg)', r'\1.webp', new_content, flags=re.IGNORECASE)
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated references in {file}")

if __name__ == "__main__":
    update_html_references()
    print("Done updating HTML references.")
