import numpy as np
import cv2

from get_image import save_image



def harris_corner_detection(reference_image):
    grayscale_image = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    grayscale_image = np.float32(grayscale_image)
    harris_image = cv2.cornerHarris(grayscale_image, 2, 3, 0.04)
    harris_image = cv2.dilate(harris_image, None)
    reference_image[harris_image > 0.01 * harris_image.max()] = [0, 0, 255]
    save_image(reference_image, "assignment_4/solutions/harris.png")




def run_harris_corner_detection(reference_image):
    harris_corner_detection(reference_image)