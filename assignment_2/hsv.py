import numpy as np
import cv2
from image import save_image


# Converts the image to HSV
def hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    save_image(hsv_image, "assignment_2/solutions/iris-1_hsv.png")


def hsv_message():
    print("Image converted to HSV color space successfully.\n")


def run_hsv(image):
    hsv(image)
    hsv_message()
