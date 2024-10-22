import cv2

def apply_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)
