from get_image import read_image
from harris_corner_detection import run_harris_corner_detection
from image_alignment import run_image_alignment



def greet_message():
    print("Lab assignment 4 - Local features matching and Harris corner detection")


def main():
    greet_message()

    reference_image = read_image()
    run_harris_corner_detection(reference_image)
    run_image_alignment()


if __name__ == "__main__":
    main()