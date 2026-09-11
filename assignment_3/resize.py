import cv2

from get_image import save_image


def resize(image, scale_factor: int, up_or_down: str):

    image_resized = image 

    if up_or_down == 'up':
        for i in range(scale_factor):
            row, col = image_resized.shape[:2]
            image_resized = cv2.pyrUp(image_resized, dstsize=(col * 2, row * 2))
    elif up_or_down == 'down':
        for i in range(scale_factor):
            row, col = image_resized.shape[:2]
            image_resized = cv2.pyrDown(image_resized, dstsize=(col // 2, row // 2))

    save_image(image_resized, "assignment_3/solutions/resize.png")


def run_resize(image): 
    resize(image, 2, 'up') # upsample the image by a factor of 2