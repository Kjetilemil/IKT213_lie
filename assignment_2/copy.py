import numpy as np
from image import save_image



# Function for copying an image
# height, width, channels = image.shape, gets the dimention of the omage
# emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8), creates a new black image
# emptyPictureArray[:] = image[:], creates a copy of the first image to the new black image created
def copy(image, emptyPictureArray):

    height, width, channels = image.shape

    emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
    emptyPictureArray[:] = image[:]
    save_image(emptyPictureArray, "assignment_2/solutions/iris-1_copied.png")


def copy_message():
    print("Image copied successfully.\n")


def run_copy(image, emptyPictureArray):
    copied_image = copy(image, emptyPictureArray)
    copy_message()
    return copied_image
