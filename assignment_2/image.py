
import numpy as np
import cv2



# read the image
def read_image():
    image_data = cv2.imread("assignment_2/images/iris-1.png")
    return image_data


# display the original image size
def display_original_image_size(image):
    height, width = image.shape[:2]
    print(f"Original image size: {width}x{height} pixels.\n")


# function to save the image after processing
def save_image(image, img_path):

    saved = cv2.imwrite(img_path, image)
    if saved:
        print("Image processed and saved successfully.")
    else:
        print("Error saving image.")
    return saved


def run_display_original_image():
    image = read_image() # read the image
    display_original_image_size(image) # display the original image size
    return image