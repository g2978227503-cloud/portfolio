import os
import glob
from PIL import Image

def convert_to_webp(directory):
    # Find all png and jpg files
    types = ('*.png', '*.jpg', '*.jpeg')
    files_to_convert = []
    
    for ext in types:
        files_to_convert.extend(glob.glob(os.path.join(directory, '**', ext), recursive=True))
        
    total_saved_bytes = 0
    converted_count = 0
    
    for file_path in files_to_convert:
        # Skip if already a webp
        if file_path.lower().endswith('.webp'):
            continue
            
        original_size = os.path.getsize(file_path)
        
        # Don't convert very small images (e.g. less than 10KB) as WebP might actually increase size
        if original_size < 10240:
            continue
            
        try:
            # Open image
            img = Image.open(file_path)
            
            # Create new filename with .webp extension
            base = os.path.splitext(file_path)[0]
            new_file_path = base + '.webp'
            
            # Convert RGBA to RGB if saving as JPEG-like WebP (lossy)
            # WebP supports alpha channel, so we can keep it for PNGs
            
            # Save as WebP
            # quality=85 is a good balance between size and quality
            img.save(new_file_path, 'webp', quality=85, method=6)
            
            new_size = os.path.getsize(new_file_path)
            
            # If WebP is smaller, keep it and delete original
            if new_size < original_size:
                os.remove(file_path)
                saved_bytes = original_size - new_size
                total_saved_bytes += saved_bytes
                converted_count += 1
                print(f"Converted {os.path.basename(file_path)} -> {os.path.basename(new_file_path)}")
                print(f"  Size: {original_size/1024:.1f}KB -> {new_size/1024:.1f}KB (Saved {saved_bytes/1024:.1f}KB)")
            else:
                # If WebP is larger, delete the new WebP and keep original
                os.remove(new_file_path)
                print(f"Skipped {os.path.basename(file_path)} (WebP was larger)")
                
        except Exception as e:
            print(f"Error converting {file_path}: {e}")
            
    print("-" * 40)
    print(f"Total files converted: {converted_count}")
    print(f"Total space saved: {total_saved_bytes / (1024*1024):.2f} MB")

if __name__ == "__main__":
    images_dir = os.path.join(os.getcwd(), 'images')
    if os.path.exists(images_dir):
        print(f"Starting conversion in {images_dir}...")
        convert_to_webp(images_dir)
    else:
        print("Images directory not found!")
