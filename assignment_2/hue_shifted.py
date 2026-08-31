import numpy as np
import cv2
from image import save_image


# Adds specific HUE to the image
# emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8), creates an empty black image
# array_hue = np.full((height, width, 3), hue, dtype=np.uint8), makes a new array with specified HUE
# emptyPictureArray[:] = cv2.add(image, array_hue), adds array_hue to the image
def hue_shifted(image, emptyPictureArray, hue):

    height, width, channels = image.shape
    
    emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
    array_hue = np.full((height, width, 3), hue, dtype=np.uint8)
    emptyPictureArray[:] = cv2.add(image, array_hue)

    save_image(emptyPictureArray, "assignment_2/solutions/iris-1_hue_shifted.png") 

def hue_shifted_message():
    print("Hue shifted image saved successfully.\n")


def run_hue_shifted(image):
    hue_shifted(image, None, 50) # changes the hue of the image by 50 
    hue_shifted_message()

