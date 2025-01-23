import os
import csv

def get_label(dataset_path, output_csv):
    label_mapping = {
        'Cat': 0,
        'Dog': 1
    }

    with open(output_csv, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['filename', 'label'])

        for category, label in label_mapping.items():
            folder_path = os.path.join(dataset_path, category)
            if os.path.exists(folder_path):
                for image_name in os.listdir(folder_path):
                    image_path = os.path.join(folder_path, image_name)
                    if image_name.endswith(('jpg' ,'jpeg', 'png')):
                        print(f"Writing {image_path} with label {label}")
                        csv_writer.writerow([image_path, label])
            else:
                print(f"Folder {folder_path} does not exist")
    print(f"Label file is saved as {output_csv}")

dataset_path = 'dataset'
output_csv = 'label.csv'
get_label(dataset_path, output_csv)
