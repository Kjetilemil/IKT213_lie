import numpy as np
import cv2

from get_image import save_image


def canny_edge_detection(image, threshold_1, threshold_2):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 1. Convert the image to grayscale
    blurred_image = cv2.GaussianBlur(grayscale_image, (3, 3), 0) # 2. Blur the image to reduce noise
    edges = cv2.Canny(blurred_image, threshold_1, threshold_2)

    save_image(edges, "assignment_3/solutions/canny_edge.png") # 3. Save the resulting image to a file


def run_canny_edge_detection(image):
    canny_edge_detection(image, 50, 50)