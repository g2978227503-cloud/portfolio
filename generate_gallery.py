import os
import urllib.parse

root_dir = "images/system-netease"

def generate_html(directory):
    html = ""
    # Sort for consistent order
    for root, dirs, files in sorted(os.walk(directory)):
        files = sorted([f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])
        if not files:
            continue
            
        rel_path = os.path.relpath(root, directory)
        if rel_path == ".":
            section_title = "Overview"
        else:
            section_title = os.path.basename(root)
            
        html += f'<div class="gallery-section">\n'
        html += f'  <h3 class="gallery-title">{section_title}</h3>\n'
        html += f'  <div class="gallery-grid">\n'
        
        for file in files:
            file_path = os.path.join(root, file)
            # URL encode the path for HTML src
            url_path = urllib.parse.quote(file_path)
         import os
import urllib.parse

root_dir = "im">import u
 
root_dir = "image f