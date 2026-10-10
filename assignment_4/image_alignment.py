import numpy as np
import cv2

from get_image import save_image

def image_alignment(image_to_align, reference_image, max_features, good_match_percent):
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(image_to_align, None)
    kp2, des2 = sift.detectAndCompute(reference_image, None)


    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good = []
    for m, n in matches:
        if m.distance < good_match_percent * n.distance:
            good.append(m)

    if len(good) > max_features:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
        h, w = reference_image.shape
        aligned_image = cv2.warpPerspective(image_to_align, M, (w, h))
        save_image(aligned_image, 'assignment_4/solutions/aligned.jpg')
    else:
        print("Not enough good matches found for alignment.")
        matches_mask = None

    draw_params = dict(matchColor=(0, 255, 0), singlePointColor=None, matchesMask=matches_mask, flags=2)
    matched_image = cv2.drawMatches(image_to_align, kp1, reference_image, kp2, good, None, **draw_params)
    save_image(matched_image, 'assignment_4/solutions/matches.jpg')







def run_image_alignment():
    print("Feature matching and image alignment using SIFT and FLANN-based matcher")
    image_to_align = cv2.imread('assignment_4/image/align_this.jpg', cv2.IMREAD_GRAYSCALE)
    reference_image = cv2.imread('assignment_4/image/reference_img.png', cv2.IMREAD_GRAYSCALE)
    image_aligned = image_alignment(image_to_align, reference_image, 10, 0.7)