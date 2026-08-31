import numpy as np

from crop import run_crop 
from padding import run_padding
from image import run_display_original_image, save_image 
from resize import run_resize
from copy import run_copy
from grayscale import run_grayscale
from hsv import run_hsv
from hue_shifted import run_hue_shifted
from smoothing import run_smoothing
from rotation import run_rotation


def greet():
    print("\nLab assignment 2 - Basic imaging operations and applying linear filters with OpenCV\n")


def main():

    greet()
    image = run_display_original_image() # read the image
    run_padding(image) # padding
    run_crop(image) # crop
    run_resize(image) # resize
    run_copy(image, None) # copy
    run_grayscale(image) # grayscale
    run_hsv(image) # HSV color
    run_hue_shifted(image) # hue
    run_smoothing(image) # smoothing
    run_rotation(image) # rotate 

if __name__ == '__main__':
    main()