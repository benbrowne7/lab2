import numpy as np
import cv2
import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Convert RGB to GRAY')
parser.add_argument('-name', '-n', type=str, default='car2.png')
parser.add_argument('-size', '-s', type=int, default=5)
args = parser.parse_args()

iname = args.name
size = args.size

image = cv2.imread(iname, cv2.IMREAD_UNCHANGED)

img_median = cv2.medianBlur(image, size)

cv2.imwrite("median.jpg", img_median);



