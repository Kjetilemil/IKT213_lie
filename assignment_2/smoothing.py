import numpy as np
import cv2
from image import save_image



# Function to smooth the image
# blurred_image = cv2.GaussianBlur(image,(15,15 ),0), is a function to make the blur happen (Gaussian blur)
def smoothing (image):

    blurred_image = cv2.GaussianBlur(image,(15,15 ),0)
    save_image(blurred_image, "assignment_2/solutions/iris-1_smoothed.png")


def smoothing_message():
    print("Smoothing applied successfully.\n")



def run_smoothing(image):
    smoothing(image)
    smoothing_message()