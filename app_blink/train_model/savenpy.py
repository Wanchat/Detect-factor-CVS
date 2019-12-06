from imutils import paths
import random
import cv2
import os
import argparse
from argparse import ArgumentParser
import numpy as np
from tensorflow.python.keras.preprocessing.image import img_to_array

# ap = ArgumentParser()
# ap.add_argument("-d", "--dataset", required=True, help="path of images")
# args = vars(ap.parse_args())

PATH_IMAGE = r"D:\blink_data"

data = []
labels = []

imagePaths = sorted(list(paths.list_images(PATH_IMAGE)))
random.seed(64)
random.shuffle(imagePaths)

for imagePath in imagePaths:

    # print(imagePath)
    
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    data.append(image)

    label = imagePath.split(os.path.sep)[-2]
    label = 1 if label == "openeyes" else 0
    labels.append(label)

data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

np.save(r"npy/data_blinks_color.npy",data)
np.save(r"npy/label_blinks_color.npy",labels)

print("save npy to >>> drive")









