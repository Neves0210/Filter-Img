import streamlit as st
import cv2
import numpy as np
from filters.grayscale import apply_grayscale
from filters.blur import apply_blur
from filters.edge_detection import apply_edge_detection
from filters.sharpen import apply_sharpen
from filters.sobel import apply_sobel

@st.cache_data
def load_image(image_file):
    return cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

def ensure_bgr(image):
    return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR) if len(image.shape) == 2 else image

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

def convert_image_for_download(image, file_format, quality):
    if file_format == 'jpg':
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    else:
        encode_param = [int(cv2.IMWRITE_PNG_COMPRESSION), 9 - int(quality / 10)]
    
    _, buffer = cv2.imencode(f".{file_format}", image, encode_param)
    return buffer.tobytes()

st.title("Editor de Imagens com Filtros")
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    original_image = load_image(uploaded_file)

    filter_option = st.selectbox("Escolha um filtro:", ("Grayscale", "Blur", "Edge Detection", "Sharpen", "Sobel"))

    edited_image = apply_filter(filter_option, original_image)

    view_option = st.sidebar.radio("Como você gostaria de visualizar a imagem?", ("Deslizar para ver a imagem", "Imagem Completa"))

    if view_option == "Deslizar para ver a imagem":
        slider_value = st.slider("Deslize para revelar a imagem editada", 0, 100, 50)
        alpha = slider_value / 100.0
        edited_image_bgr = ensure_bgr(cv2.resize(edited_image, (original_image.shape[1], original_image.shape[0])))

        combined_image = cv2.addWeighted(original_image, 1 - alpha, edited_image_bgr, alpha, 0)
        st.image(combined_image, channels="BGR")

    else:
        col1, col2 = st.columns(2)
        with col1:
            st.image(ensure_bgr(original_image), caption="Imagem Original", channels="BGR")
        with col2:
            st.image(ensure_bgr(edited_image), caption="Imagem Editada", channels="BGR")

    st.subheader("Baixar Imagem Editada")
    file_format = st.selectbox("Escolha o formato do arquivo:", ("jpg", "png"))


    if file_format == 'jpg':
        quality = st.slider("Escolha a qualidade da imagem (JPEG)", 1, 100, 90)
    else:
        quality = st.slider("Escolha o nível de compressão (PNG)", 0, 9, 9)

    edited_image_bgr = ensure_bgr(edited_image)


    image_data = convert_image_for_download(edited_image_bgr, file_format, quality)

    st.download_button(
        label="Baixar Imagem",
        data=image_data,
        file_name=f"imagem_editada.{file_format}",
        mime=f"image/{file_format}"
    )
