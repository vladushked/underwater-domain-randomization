import glob
import os
import numpy as np
from pathlib import Path
import shutil

def copy_fake_images(fake_images, to_dir):
    for fake_image_path in fake_images:
        image_name = os.path.split(fake_image_path)[-1]
        new_name = "".join(image_name.split("_fake"))
        shutil.copy2(fake_image_path, os.path.join(to_dir, new_name))

train_path = "/home/vladushked/Downloads/images"
val_path = "/home/vladushked/Downloads/images"
out_train_dir = "/home/vladushked/Documents/data/unity/round_gan/train/images"
out_val_dir = "/home/vladushked/Documents/data/unity/round_gan/eval/images"
Path(out_train_dir).mkdir(parents=True, exist_ok=True)
Path(out_val_dir).mkdir(parents=True, exist_ok=True)
train_images = glob.glob(os.path.join(train_path, "*fake.png"))
val_images = glob.glob(os.path.join(val_path, "*fake.png"))

copy_fake_images(train_images, out_train_dir)
copy_fake_images(val_images, out_val_dir)