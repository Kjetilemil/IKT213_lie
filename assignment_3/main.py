import numpy as np
import cv2

from get_image import read_image
from sobel_edge import run_sobel_edge_detection
from canny_edge import run_canny_edge_detection
from template_match import run_template_matching
from resize import run_resize


def greet_message():
    print("\nLab assignment 3 - Edge detection, Image resampling, and Template matching\n")


def main():

    greet_message()
    image = read_image() # read the image
    run_sobel_edge_detection(image)
    run_canny_edge_detection(image)
    run_template_matching()
    run_resize(image)

if __name__ == '__main__':
    main()