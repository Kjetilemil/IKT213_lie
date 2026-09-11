import numpy as np
import cv2


def read_image():
    image_data = cv2.imread("assignment_3/image/lambo.png")
    if image_data is None:
        print("Could not read the image")
    else:
        print("Image read successfully") 
        return image_data

    

def save_image(image, img_path):
    saved = cv2.imwrite(img_path, image)
    if saved:
        print("Image saved successfully")
    else:
        print("Failed to save the image")
    return saved