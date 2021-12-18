# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 08:39:00 2021

@author: NUGI
"""

import cv2
import numpy as np

#import yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f :
    classes


    