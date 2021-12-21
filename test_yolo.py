# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 08:39:00 2021

@author: NUGI
"""

import cv2
import numpy
import glob

folders = glob.glob(r'C:\Users\NUGI\Downloads\Belajar DM\nyoba_YOLO\Dataset\kucing_set\training_set\cats')
image_files = []
for folder in folders:
    for f in glob.glob(folder+'/*.jpg'):
        image_files.append(f)

for image_file in image_files:
    print(f"Displaying image with Image Name: {image_file}")
    display(Image(filename=f"{image_file}"))

import os
dir_name = "images_with_boxes"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

import cvlib as cv
for image_file in image_files:
    from cvlib.object_detection import draw_bbox
    """Detects common objects on an image and creates a new image with bounding boxes.
    Args:
        filename (str): Filename of the image.
        model (str): Either "yolov3" or "yolov3-tiny". Defaults to "yolov3-tiny".
        confidence (float, optional): Desired confidence level. Defaults to 0.6.
    """
    # Images are stored under the images/ directory
    img_filepath = f'{filename}'
    # Read the image into a numpy array
    img = cv2.imread(img_filepath)
    # Perform the object detection
    bbox, label, conf = cv.detect_common_objects(img, confidence=0.6, model="yolov3-tiny")
    # Print current image's filename
    print(f"========================nImage processed: {filename}n")
    # Print detected objects with confidence level
    for l, c in zip(label, conf):
        print(f"Detected object: {l} with confidence level of {c}n")
    # Create a new image that includes the bounding boxes
    output_image = draw_bbox(img, bbox, label, conf)
    # Save the image in the directory images_with_boxes
    cv2.imwrite(f'images_with_boxes/{filename}', output_image)
    # Display the image with bounding boxes
    display(Image(f'images_with_boxes/{filename}'))  