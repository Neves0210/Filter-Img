import cv2

def apply_edge_detection(image, low_threshold=50, high_threshold=150):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray_image, low_threshold, high_threshold)
