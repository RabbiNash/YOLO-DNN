# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

print(cv2.__version__)

img = cv2.imread('test_images/FANTRACKER.jpeg')

cv2.imshow("Test", img )