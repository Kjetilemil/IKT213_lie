
import numpy as np
import cv2
from image import save_image



# function to resize the image 
# the src variable stores the original image 
# resized_image = cv2.resize(src_image, (width, height)), is a function to resize the image. 
def resize(image, width, height):

    src_image = image
    resized_image = cv2.resize(src_image, (width, height))
    save_image(resized_image, "assignment_2/solutions/iris-1_resized.png")
    display_resized_image_size(resized_image)


# display the resized image size
def display_resized_image_size(image):
    height, width = image.shape[:2]
    print(f"Resized image size: {width}x{height} pixels.\n")


def run_resize(image):
    resize(image, 200, 200) # resize the image to the specified dimensions