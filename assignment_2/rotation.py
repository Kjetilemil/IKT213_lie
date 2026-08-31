import numpy as np
import cv2
from image import save_image




# Function to rotate the image 
# rotated_image = cv2.rotate(image, cv2.ROTATE_180), is a function to rotate the image 180 degrees
def rotation(image, rotation_angle):

    if rotation_angle == 90:
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        save_image(rotated_image, "assignment_2/solutions/iris-1_rotated_90.png")
    elif rotation_angle == 180:
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)
        save_image(rotated_image, "assignment_2/solutions/iris-1_rotated_180.png")



def rotation_message(rotation_image):
    if rotation_image == 90:
        print("Rotation with 90 degrees applied successfully\n")
    elif rotation_image == 180:
        print("Rotation with 180 degrees applied successfully")


def run_rotation(image):
    rotation(image, 180) # rotate the image by 180 degrees
    rotation_message(180)