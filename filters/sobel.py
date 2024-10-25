import cv2
import numpy as np

def apply_sobel(image):
    """Aplica o filtro Sobel para detectar bordas em direções X e Y e calcula a magnitude."""
    # Converte para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica o filtro Sobel para as direções X e Y com maior controle de detalhes
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Calcula a magnitude e normaliza para valores de pixel padrão
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    sobel_magnitude = np.uint8(np.clip(sobel_magnitude, 0, 255))
    
    return sobel_magnitude
