import numpy as np
import cv2

from get_image import save_image


def sobel_edge_detection(image):

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 1. Convert the image to grayscale
    blurred_image = cv2.GaussianBlur(grayscale_image, (3, 3), 0) # 2. Blur the image to reduce noise
    sobelimage_x = cv2.Sobel(src=blurred_image, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=1) # 3. Apply the Sobel operator with dx=1, dy=0, ksize=1
    sobelimage_y = cv2.Sobel(src=blurred_image, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=1) # 3. Apply the Sobel operator with dx=0, dy=1, ksize=1
    sobel_image = cv2.magnitude(sobelimage_x, sobelimage_y)
    normalized_sobel_image = cv2.normalize(sobel_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8) # Normalize the result to the range [0, 255]
    save_image(normalized_sobel_image, "assignment_3/solutions/sobel_edge.png") # 4. Save the resulting image to a file


def run_sobel_edge_detection(image):
    sobel_edge_detection(image) 