import numpy as np
from image import save_image


# image[y_0:y_1, x_0:x_1] crops out a portion of the image. 
def crop(image, x_0, x_1, y_0, y_1):

    cropped_image = image[y_0:y_1, x_0:x_1]
    save_image(cropped_image, "assignment_2/solutions/iris-1_cropped.png")
    display_cropped_image_size(cropped_image)



# display the cropped image size
def display_cropped_image_size(image):
    height, width = image.shape[:2]
    print(f"Cropped image size: {width}x{height} pixels.\n")


def run_crop(image):
    crop(image, 200, 670, 200, 470) # crop the image with the specified coordinates
    