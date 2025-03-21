import pytesseract
from PIL import Image
import cv2
import json
import os
import re
import numpy as np
import glob

def find_menu_file():
    # Look for JPG, JPEG, or PDF files in the 'uploads' directory
    supported_files = glob.glob('uploads/*.[jJ][pP][gG]') + glob.glob('uploads/*.[jJ][pP][eE][gG]') + glob.glob('uploads/*.[pP][dD][fF]')
    return supported_files[0] if supported_files else None

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def parse_menu_text(raw_text):
    lines = raw_text.split('\n')
    items = []
    for line in lines:
        match = re.match(r'^(.*?)\s+\$?(\d{1,3})$', line.strip())
        if match:
            name = match.group(1).strip()
            price = int(match.group(2))
            items.append({
                "name": name,
                "price": price,
                "ingredients": [],
                "image": "images/placeholder.jpg"
            })
    return items

def generate_json(menu_items, restaurant_name="SAKU Sushi Thai & Hibachi", category_name="Specialty Rolls"):
    return {
        "restaurant": restaurant_name,
        "categories": [
            {
                "name": category_name,
                "items": menu_items
            }
        ]
    }

def save_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

def grid_based_image_extraction(image_path, output_dir, menu_items, grid_rows, grid_cols):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    cell_height = height // grid_rows
    cell_width = width // grid_cols

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, item in enumerate(menu_items):
        r = i // grid_cols
        c = i % grid_cols
        y1, y2 = r * cell_height, (r + 1) * cell_height
        x1, x2 = c * cell_width, (c + 1) * cell_width

        cropped_img = image[y1:y2, x1:x2]
        dish_name_sanitized = re.sub(r'[^a-zA-Z0-9_\-]', '_', item['name'])
        img_path = os.path.join(output_dir, f'{dish_name_sanitized}.jpg')
        cv2.imwrite(img_path, cropped_img)
        item['image'] = img_path

def main():
    input_image = find_menu_file()

    if not input_image:
        print("No JPG, JPEG, or PDF menu found in uploads directory.")
        return

    print(f"Using menu file: {input_image}")

    print("Extracting text from image...")
    extracted_text = extract_text_from_image(input_image)

    print("Parsing menu items...")
    menu_items = parse_menu_text(extracted_text)

    print("Performing grid-based image extraction...")
    grid_based_image_extraction(input_image, 'images/extracted/', menu_items, grid_rows=4, grid_cols=5)  # Adjust rows/cols as needed

    print("Generating menu.json...")
    menu_json = generate_json(menu_items)
    save_json(menu_json, 'menu.json')

    print(f"menu.json created successfully with {len(menu_items)} items.")

if __name__ == "__main__":
    main()