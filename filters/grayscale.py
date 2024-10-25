import cv2

def apply_grayscale(image):
    """Converte a imagem para escala de cinza, com conversão padrão de cores."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
