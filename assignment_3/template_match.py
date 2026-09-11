import numpy as np
import cv2

from get_image import save_image


def template_match(image, template):
    grayscale_shapes = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale
    img_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY) # Convert the template to grayscale
    width, height = img_template.shape[::-1] # Get the width and height of the template

    result = cv2.matchTemplate(grayscale_shapes, img_template, cv2.TM_CCOEFF_NORMED) # Perform template
    threshold = 0.9 
    locations = np.where(result >= threshold) #Find locations where the matching result exceeds the threshold
    for point in zip(*locations[::-1]): # Draw rectangles around the matched regions
        cv2.rectangle(image, point, (point[0] + width, point[1] + height), (0, 0, 255), 2)
    save_image(image, "assignment_3/solutions/template_match.png") # Save the resulting image to a file  


def run_template_matching():
    image = cv2.imread("assignment_3/image/shapes-1.png")
    template = cv2.imread("assignment_3/image/shapes_template.jpg")
    template_match(image, template)