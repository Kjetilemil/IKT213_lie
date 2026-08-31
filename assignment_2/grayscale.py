
import numpy as np
import cv2
from image import save_image


# Makes the image gray
def grayscale(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    save_image(grayscale_image, "assignment_2/solutions/iris-1_grayscale.png")


def grayscale_message():
    print("Image converted to grayscale successfully.\n")


def run_grayscale(image):
    grayscale(image)
    grayscale_message()
