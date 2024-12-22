import os
from PIL import Image
def load_flickr30k_images(image_folder):
    images = []
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust for image formats
            image_path = os.path.join(image_dir, filename)
            try:
                img = Image.open(image_path)
                images.append(img)
            except Exception as e:
                print(f"Error loading image {filename}: {e}")
    
    return images

def load_flickr30k_captions(file_path):
    captions = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or ', ' not in line:
                continue

            try:
                # Split by the first comma to separate the image filename from the caption
                image_filename, caption = line.split(', ', 1)
                # Append the caption to the list of captions for the image
                if image_filename in captions:
                    captions[image_filename].append(caption)
                else:
                    captions[image_filename] = [caption]
            except ValueError:
                print(f"Skipping line: {line}")  # Log invalid lines if needed
    return captions

