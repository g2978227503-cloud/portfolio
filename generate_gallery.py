import os
import urllib.parse

# Define the root structure we want to traverse
structure = {
    "提升设计效率": {
        "path": "images/system-netease/efficiency",
        "subsections": {
            "活动模版型管线": "template",
            "资源位型管线": "resource",
            "长图H5型管线": "h5"
        }
    },
    "提升设计质量": {
        "path": "images/system-netease/quality",
        "subsections": {
            "手绘型需求管线": "hand-drawn"
        }
    }
}

def generate_html():
    html = ""
    
    for section_name, section_info in structure.items():
        html += f'<section class="detail-section">\n'
        html += f'    <h2 class="section-title">{section_name}</h2>\n'
        
        base_path = section_info["path"]
        subsections = section_info["subsections"]
        
        for sub_name, sub_dir in subsections.items():
            full_path = os.path.join(base_path, sub_dir)
            if not os.path.exists(full_path):
                continue
                
            html += f'    <div class="gallery-group">\n'
            html += f'        <h3 class="gallery-subtitle">{sub_name}</h3>\n'
            html += f'        <div class="gallery-grid">\n'
            
            # Walk through the directory to find images
            image_files = []
            for root, dirs, files in os.walk(full_path):
                for file in files:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        # Calculate relative path from project root
                        rel_path = os.path.join(root, file)
                        image_files.append(rel_path)
            
            # Sort to keep consistent order
            image_files.sort()
            
            for img_path in image_files:
                # URL encode the path parts but keep slashes
                parts = img_path.split('/')
                encoded_parts = [urllib.parse.quote(p) for p in parts]
                url = "/".join(encoded_parts)
                
                html += f'            <div class="gallery-item">\n'
                html += f'                <img src="{url}" alt="{os.path.basename(img_path)}" loading="lazy">\n'
                html += f'            </div>\n'
                
            html += f'        </div>\n'
            html += f'    </div>\n'
            
        html += f'</section>\n'
            
    return html

if __name__ == "__main__":
    print(generate_html())
