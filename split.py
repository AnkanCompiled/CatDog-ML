import os
import shutil
import random

def split_dataset(source_dir, train_dir, val_dir, test_dir, split_r):
    for category in ['Cat', 'Dog']:
        category_path = os.path.join(source_dir, category)
        images = os.listdir(category_path)
        random.shuffle(images)
        train_split = int(len(images) * split_r[0])
        val_split = int(len(images) * (split_r[0] + split_r[1]))

        train_images = images[:train_split]
        val_images = images[train_split:val_split]
        test_images = images[val_split:]
        
        os.makedirs(os.path.join(train_dir, category), exist_ok=True)
        os.makedirs(os.path.join(val_dir, category), exist_ok=True)
        os.makedirs(os.path.join(test_dir, category), exist_ok=True)

        for img in train_images:
            print(f"Copying {img} to {train_dir}/{category}")
            shutil.copy(os.path.join(category_path, img), os.path.join(train_dir, category))
        for img in val_images:
            print(f"Copying {img} to {train_dir}/{category}")
            shutil.copy(os.path.join(category_path, img), os.path.join(val_dir, category))
        for img in test_images:
            print(f"Copying {img} to {train_dir}/{category}")
            shutil.copy(os.path.join(category_path, img), os.path.join(test_dir, category))

    print(f"Images are split into {train_dir}, {val_dir}, {test_dir}")



source_dir = 'dataset'
train_dir = 'dataset/train'
validation_dir = 'dataset/validation'
test_dir = 'dataset/test'

split_ratio = (0.7, 0.2, 0.1)

split_dataset(source_dir, train_dir, validation_dir, test_dir, split_ratio)