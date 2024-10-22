import cv2

def apply_edge_detection(image):
    return cv2.Canny(image, 100, 200)
