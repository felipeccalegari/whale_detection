# USED TO FILTER THE ORIGINAL DATASET FROM "HAPPY WHALE" CHALLENGE TO ONLY HUMPBACK WHALES

import os
import csv

# === CONFIGURE THESE ===
csv_file = 'filtered_data_new.csv'                   # Your original CSV file
images_folder = 'train_images/'              # Folder with images (trailing slash)
new_csv_file = 'humpback_only.csv'     # Output CSV to keep only humpback_whale entries

# === MAIN SCRIPT ===
with open(csv_file, 'r', newline='') as infile, open(new_csv_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)
    writer.writerow(header)  # Write header to new CSV

    for row in reader:
        if len(row) < 2:
            continue  # Skip malformed lines
        image_name, species = row[0], row[1]

        if species == 'humpback_whale':
            writer.writerow(row)  # Keep this row and image
        else:
            # Delete the image
            image_path = os.path.join(images_folder, image_name)
            if os.path.exists(image_path):
                try:
                    os.remove(image_path)
                    print(f"Deleted: {image_path}")
                except Exception as e:
                    print(f"Error deleting {image_path}: {e}")
            else:
                print(f"Not found: {image_path}")