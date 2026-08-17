import numpy as np
import cv2

# read the image
def read_image():
    image_data = cv2.imread("images/iris-1.jpg")
    return image_data


# get the size of the image and prints the correct values
def print_image_information(image):

    height, width, channels = image.shape
    size = image.size 
    data_type = image.dtype 

    print("\n")
    print("height:", height)
    print("width:", width)
    print("channels:", channels)
    print("size (number of values in the cubed array):", size) 
    print("data type:", data_type)
    print("\n")


def main():

    image = read_image()
    print_image_information(image)  


if __name__ == "__main__":
    main()