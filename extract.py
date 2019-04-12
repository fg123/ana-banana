import numpy as np
import cv2
import sys
import os

#np.set_printoptions(threshold=sys.maxsize)
file = sys.argv[1]
base = os.path.splitext(file)[0]

image = cv2.imread(file)

def is_white(pixel):
	return np.all(pixel > 250)

def column_all_white(column):
	return np.all(np.array([is_white(p) for p in column]))

height, width = image.shape[:2]

last_all_white = False
start_col = 0

next_id = 0

try:
    os.stat(base)
except:
    os.mkdir(base)

def make_image(start, end, id):
    new_image = image[0:height, start:end]
    # Remove top and bottom white
    sh = 0
    while (column_all_white(new_image[sh])):
        sh += 1
    eh = height
    while (column_all_white(new_image[eh - 1])):
        eh -= 1
    new_image = image[sh:eh, start:end]
    cv2.imshow('image', new_image)
    cv2.waitKey(0)
    new_path = base + "/" + str(id) + ".bmp"
    print("Wrote to " + new_path)
    cv2.imwrite(new_path, new_image)

for i in range(width):
    all_white = column_all_white(image[:, i])
    if (last_all_white and not all_white):
        # Start a new one
        start_col = i
    elif (not last_all_white and all_white):
        # End previous one
        make_image(start_col, i, next_id)
        next_id += 1
    last_all_white = all_white

make_image(start_col, width, next_id)
