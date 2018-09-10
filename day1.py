import os
from PIL import Image
from PIL import ImageOps
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd

%matplotlib inline

def draw_histogram(image_path):
    mt_img = Image.open(image_path)
    array = np.asarray(mt_img)
    plt.hist(array.flatten())
    plt.show()

def get_normalized_array_for_image(image_path):
    desired_size = 128
    im = Image.open(image_path)
    old_size = im.size

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    im = im.resize(new_size, Image.ANTIALIAS)

    new_im = Image.new("RGB", (desired_size, desired_size), (255,255,255))
    new_im.paste(im, ((desired_size-new_size[0])//2,
                    (desired_size-new_size[1])//2))

    new_im = ImageOps.autocontrast(new_im)
    
    array = np.asarray(new_im)
    
    return array
    
def normalize_and_copy_image(image_path, result_image_path):
    desired_size = 128
    im = Image.open(image_path)
    old_size = im.size

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    im = im.resize(new_size, Image.ANTIALIAS)

    new_im = Image.new("RGB", (desired_size, desired_size), (255,255,255))
    new_im.paste(im, ((desired_size-new_size[0])//2,
                    (desired_size-new_size[1])//2))

    new_im = ImageOps.autocontrast(new_im)
    
    new_im.save(result_image_path, 'JPEG', quality=100)

def process_and_save_all_images(starting_dir, result_dir):
    if not(os.path.exists(result_dir)):
        os.mkdir(result_dir)

    subdirs = os.listdir(starting_dir)

    for dir in subdirs:
        if not(os.path.exists(result_dir + "/" + dir)):
            os.mkdir(result_dir + "/" + dir)
        print("Directory: " + dir)
        files = os.listdir(starting_dir + "/" + dir)
        for file in files:
            source_file = starting_dir + "/" + dir + "/" + file
            result_file = result_dir + "/" + dir + "/" + file
            normalize_and_copy_image(source_file, result_file)

def create_csv_from_images(images_dir):
    subdirs = os.listdir(images_dir)
    
    numbers = []

    for dir in subdirs:
        print("Directory: " + dir)
        files = os.listdir(starting_dir + "/" + dir)
        for file in files:
            source_file = starting_dir + "/" + dir + "/" + file
            file_array = get_normalized_array_for_image(source_file)
            numbers.append(file_array)
     
    return numbers,subdirs
    
starting_dir = "./gear_images/"
result_dir = "./gear_images_normalized/"            

numbers, subdirs = create_csv_from_images(starting_dir)
