import cv2

def apply_blur(image, kernel_size=15):
    """Aplica um desfoque gaussiano com um tamanho de kernel ajustável para maior controle."""
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)