import numpy as np
import cv2

# read the image
def read_image():
    image_data = cv2.imread("assignment_1/images/iris-1.jpg")
    return image_data


# get the size of the image and prints the correct values
def print_image_information(image):

    height, width, channels = image.shape
    size = image.size 
    data_type = image.dtype 

    print("\n")
    print("IMAGE INFORMATION:")
    print("height:", height)
    print("width:", width)
    print("channels:", channels)
    print("size (number of values in the cubed array):", size) 
    print("data type:", data_type)
    print("\n")


# capture video from web camera
def capture_webcamera():
    video_data = cv2.VideoCapture(0)
    return video_data

# gets data from the image 
def get_camera_data(video_data):
    width = int(video_data.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_data.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_data.get(cv2.CAP_PROP_FPS))
    video_data.release()
    return height, width, fps


# writes data to text file 
def write_data(height, width, fps):
    with open('assignment_1/solutions/camera_outputs.txt', 'w') as file:
         file.write("VIDEO INFORMATION: \n")
         file.write(f"Height: {height}\n")
         file.write(f"Width: {width}\n")
         file.write(f"fps: {fps}")
    

def main():

    # image 
    image = read_image()
    print_image_information(image)  


    # webcamera 
    camera = capture_webcamera()
    video_height, video_width, fps = get_camera_data(camera)
    write_data(video_height, video_width, fps)

if __name__ == "__main__":
    main()