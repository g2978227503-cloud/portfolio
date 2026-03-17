import os
import re

# List of project files in the desired order
project_files = [
    'project-influence.html',
    'project-empowerment.html',
    'project-system-netease.html',
    'project-branding-bigo.html',
    'project-personal-app.html',
    'project-branding.html',
    'project-jd-motion.html',
    'project-ecommerce-interactive.html',
    'project-aso.html'
]

def extract_content(file_path, tag_name=None, class_name=None):
    if not os.path.exists(file_path):
        return f"<!-- File not found: {file_path} -->"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if tag_name:
        pattern = re.compile(f'<{tag_name}[^>]*>(.*?)</{tag_name}>', re.DOTALL)
        match = pattern.search(content)
        if match:
            return match.group(1)
    
    if class_name:
        # Simple regex to find blocks with specific class - this is fragile for nested divs but works for top-level sections
        # A better approach for specific sections is capturing known patterns
        sections = []
        
        # Find header
        header_match = re.search(r'<header class="project-header[^"]*".*?</header>', content, re.DOTALL)
        if header_match:
            sections.append(header_match.group(0))
            
        # Find meta
        meta_match = re.search(r'<section class="project-meta-grid[^"]*".*?</section>', content, re.DOTALL)
        if meta_match:
            sections.append(meta_match.group(0))
            
        # Find cover image/video (gallery-item)
        cover_match = re.search(r'<section class="gallery-item[^"]*".*?</section>', content, re.DOTALL)
        if cover_match:
            sections.append(cover_match.group(0))
            
        # Find all project-content sections
        content_matches = re.finditer(r'<section class="project-content[^"]*".*?</section>', content, re.DOTALL)
        for m in content_matches:
            sections.append(m.group(0))
            
        return "\n".join(sections)
        
    return ""

def get_resume_content():
    with open('resume-a4.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract style
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    style = style_match.group(1) if style_match else ""
    
    # Extract main content
    main_match = re.search(r'<main class="page"[^>]*>(.*?)</main>', content, re.DOTALL)
    main_content = main_match.group(1) if main_match else ""
    
    return style, main_content

# Get resume parts
resume_style, resume_content = get_resume_content()

# Build the full HTML
html_content = f"""<!doctype html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>高飞 (Goofy) - 作品集 Portfolio</title>
    <style>
        {resume_style}
        
        /* Additional Print Styles */
        @media print {{
            body {{ -webkit-print-color-adjust: exact; }}
            .page-break {{ page-break-before: always; }}
            .no-print {{ display: none !important; }}
        }}
        
        .project-page {{
            width: min(980px, calc(100vw - 32px));
            margin: 0 auto;
            padding: 40px 0;
            page-break-before: always;
        }}
        
        /* Reset some project styles to fit the print layout */
        .project-header {{ padding: 20px 0; border-bottom: 2px solid #000; }}
        .page-title {{ font-family: var(--font); font-size: 24px; font-weight: 600; margin: 0; }}
        
        .project-meta-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            border-bottom: 1px solid #ccc;
            margin-bottom: 20px;
        }}
        .meta-item {{ padding: 10px; border-right: 1px solid #eee; }}
        .meta-item:last-child {{ border-right: none; }}
        .meta-label {{ font-family: var(--mono); font-size: 10px; color: #666; display: block; margin-bottom: 4px; }}
        .meta-value {{ font-family: var(--font); font-size: 12px; font-weight: 500; }}
        
        .project-content {{
            display: grid;
            grid-template-columns: 1fr 3fr; /* Adjusted for print width */
            gap: 20px;
            padding: 20px 0;
            border-bottom: 1px solid #eee;
        }}
        
        .content-sidebar {{ }}
        .sidebar-title {{ font-family: var(--mono); font-size: 10px; color: #999; font-weight: 600; }}
        
        .content-body h3 {{ font-family: var(--font); font-size: 16px; margin: 0 0 10px 0; }}
        .content-body p, .content-body li {{ font-family: var(--font); font-size: 12px; line-height: 1.6; color: #333; margin-bottom: 10px; }}
        
        img, video {{ max-width: 100%; height: auto; display: block; margin-top: 10px; border: 1px solid #eee; }}
        
        /* Hide navigation elements from imported HTML */
        .site-nav, .mobile-nav, .next-project, .site-footer {{ display: none !important; }}
        
        /* Fade-in animation removal for print */
        .fade-in {{ opacity: 1 !important; transform: none !important; }}
    </style>
</head>
<body>

    <!-- Resume Section -->
    <main class="page">
        {resume_content}
    </main>

    <!-- Projects Section -->
"""

for project_file in project_files:
    print(f"Processing {project_file}...")
    project_content = extract_content(project_file, class_name="project-content")
    
    # Clean up some common navigation artifacts if regex didn't catch them
    project_content = project_content.replace('← BACK TO WORK', '')
    
    html_content += f"""
    <div class="project-page">
        {project_content}
    </div>
    """

html_content += """
</body>
</html>
"""

with open('portfolio-print.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("portfolio-print.html created successfully.")
