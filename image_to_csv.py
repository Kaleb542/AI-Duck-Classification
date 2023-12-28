import os
import csv
from PIL import Image
import numpy as np

def resize_image(image_path, target_size=(299, 299)):
    img = Image.open(image_path).convert('RGB')
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0
    return img_array

# Maps scientific name to label
scientific_name_map = {
    0: 'Anas rubripes',
    1: 'Melanitta americana',
    2: 'Bucephala albeola',
    3: 'Aythya valisineria',
    4: 'Bucephala clangula',
    5: 'Aythya marila',
    6: 'Clangula hyemalis',
    7: 'Mergus serrator',
    8: 'Melanitta perspicillata',
    9: 'Melanitta deglandi'
}

dataset_path = 'augmented_images'
csv_filename = 'dataset_augmented.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Image_Path', 'Label'])

    classes = sorted(os.listdir(dataset_path))
    for class_idx, class_name in enumerate(classes):
        class_path = os.path.join(dataset_path, class_name)
        for image_file in os.listdir(class_path):
            image_path = os.path.join(class_path, image_file)

            # Resize the image
            resized_image = resize_image(image_path)

            # Get correct scientific name from mapping
            scientific_name = scientific_name_map.get(class_idx, 'Unknown')

            # Add image path and label to CSV
            csv_writer.writerow([image_path, scientific_name])
