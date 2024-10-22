import streamlit as st
import cv2
import numpy as np
from filters.grayscale import apply_grayscale
from filters.blur import apply_blur
from filters.edge_detection import apply_edge_detection
from filters.sharpen import apply_sharpen
from filters.sobel import apply_sobel

# Função para carregar a imagem
def load_image(image_file):
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    return image

# Função para converter imagens em escala de cinza para BGR
def convert_to_bgr(image):
    if len(image.shape) == 2:  # Verifica se é uma imagem em escala de cinza
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Converte para BGR
    return image

# Configurando a interface do Streamlit
st.title("Editor de Imagens com Filtros")
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Carregar a imagem
    original_image = load_image(uploaded_file)

    # Selecionar o filtro
    filter_option = st.selectbox("Escolha um filtro:", ("Grayscale", "Blur", "Edge Detection", "Sharpen", "Sobel"))

    # Aplicar o filtro
    if filter_option == "Grayscale":
        edited_image = apply_grayscale(original_image)
    elif filter_option == "Blur":
        edited_image = apply_blur(original_image)
    elif filter_option == "Edge Detection":
        edited_image = apply_edge_detection(original_image)
    elif filter_option == "Sharpen":
        edited_image = apply_sharpen(original_image)
    elif filter_option == "Sobel":
        edited_image = apply_sobel(original_image)

    # Escolher entre ver a imagem completa ou usar o controle deslizante
    view_option = st.sidebar.radio("Como você gostaria de visualizar a imagem?", ("Deslizar para ver a imagem", "Imagem Completa"))

    if view_option == "Deslizar para ver a imagem":
        # Criar um slider para controlar a cortina
        slider_value = st.slider("Deslize para revelar a imagem editada", 0, 100, 50)

        # Calcular a opacidade
        alpha = slider_value / 100.0
        
        # Ajustar a imagem editada para o tamanho da imagem original
        edited_image_resized = cv2.resize(edited_image, (original_image.shape[1], original_image.shape[0]))

        # Garantir que ambas as imagens tenham três canais
        edited_image_bgr = convert_to_bgr(edited_image_resized)

        # Mesclar as imagens
        combined_image = cv2.addWeighted(original_image, 1 - alpha, edited_image_bgr, alpha, 0)

        # Mostrar a imagem resultante
        st.image(combined_image, channels="BGR")

    elif view_option == "Imagem Completa":
        # Exibir a imagem original e a editada lado a lado
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(convert_to_bgr(original_image), caption="Imagem Original", channels="BGR")
        
        with col2:
            edited_image_bgr = convert_to_bgr(edited_image)
            st.image(edited_image_bgr, caption="Imagem Editada", channels="BGR")
