import cv2
import numpy as np

def apply_sharpen(image):
    """Aplica um filtro de nitidez (sharpen) com kernel refinado para realçar detalhes."""
    # Ajuste do kernel para suavizar o efeito de nitidez e evitar ruídos exagerados
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)