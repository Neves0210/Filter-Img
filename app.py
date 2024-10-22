import streamlit as st
import cv2
import numpy as np
from filters.grayscale import apply_grayscale
from filters.blur import apply_blur
from filters.edge_detection import apply_edge_detection
from filters.sharpen import apply_sharpen
from filters.sobel import apply_sobel

# Função para carregar a imagem com cache
@st.cache_data
def load_image(image_file):
    return cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

# Função para garantir que a imagem tenha três canais (BGR)
def ensure_bgr(image):
    return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR) if len(image.shape) == 2 else image

# Função para aplicar filtros com cache
@st.cache_data
def apply_filter(filter_option, image):
    filters = {
        "Grayscale": apply_grayscale,
        "Blur": apply_blur,
        "Edge Detection": apply_edge_detection,
        "Sharpen": apply_sharpen,
        "Sobel": apply_sobel,
    }
    return filters[filter_option](image)

# Interface do Streamlit
st.title("Editor de Imagens com Filtros")
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Carregar a imagem
    original_image = load_image(uploaded_file)

    # Selecionar o filtro
    filter_option = st.selectbox("Escolha um filtro:", ("Grayscale", "Blur", "Edge Detection", "Sharpen", "Sobel"))

    # Aplicar o filtro selecionado
    edited_image = apply_filter(filter_option, original_image)

    # Visualização
    view_option = st.sidebar.radio("Como você gostaria de visualizar a imagem?", ("Deslizar para ver a imagem", "Imagem Completa"))

    if view_option == "Deslizar para ver a imagem":
        slider_value = st.slider("Deslize para revelar a imagem editada", 0, 100, 50)
        alpha = slider_value / 100.0
        edited_image_bgr = ensure_bgr(cv2.resize(edited_image, (original_image.shape[1], original_image.shape[0])))

        # Mesclar as imagens de acordo com o slider
        combined_image = cv2.addWeighted(original_image, 1 - alpha, edited_image_bgr, alpha, 0)
        st.image(combined_image, channels="BGR")

    else:
        col1, col2 = st.columns(2)
        with col1:
            st.image(ensure_bgr(original_image), caption="Imagem Original", channels="BGR")
        with col2:
            st.image(ensure_bgr(edited_image), caption="Imagem Editada", channels="BGR")
