
import numpy as np
import cv2
from image import save_image


# display the padded image size
def display_padded_image_size(image):
    height, width = image.shape[:2]
    print(f"Padded image size: {width}x{height} pixels.\n")


 # adds padding to the image
 # top, bottom, left, right,  sets the border size 
 # reflect = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_REFLECT), is a function to add the border
def padding(image, border_width):

    top = border_width
    bottom = border_width 
    left = border_width 
    right = border_width

    reflect = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_REFLECT)
    save_image(reflect, "assignment_2/solutions/iris-1_padded.png")
    display_padded_image_size(reflect)


def run_padding(image):
    padding(image, 100) # apply padding to the image
    