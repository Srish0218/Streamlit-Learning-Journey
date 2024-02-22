import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style ='text-align:center;'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

image = st.file_uploader("Upload Your Image", type=["png", "jpg"])

info = st.empty()
size = st.empty()
mode = st.empty()
img_format = st.empty()
if image:
    img = Image.open(image)
    st.image(img)
    info.markdown("<h2 style ='text-align:center;'>Information</h2>", unsafe_allow_html=True)
    size.markdown(f"<h6> Size: {img.size}</h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6> Mode: {img.mode}</h6>", unsafe_allow_html=True)
    img_format.markdown(f"<h6> Image Format: {img.format}</h6>", unsafe_allow_html=True)
    st.markdown("<h2 style ='text-align:center;'>Resizing</h2>", unsafe_allow_html=True)
    width = st.number_input("Width: ", value=img.width)
    height = st.number_input("Height: ", value=img.height)
    st.markdown("---")

    st.markdown("<h2 style ='text-align:center;'>Rotate</h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree: ")
    st.markdown("---")

    st.markdown("<h2 style ='text-align:center;'> Filters </h2>", unsafe_allow_html=True)
    filter_img = st.selectbox("Filters" , options= ("None" , "Blur" , "Detail" , "Emboss" , "Smooth"))

    s_btn = st.button("Submit")
    if s_btn:
        edited = img.resize((width, height)).rotate(degree)
        st.image(edited)
        filtered = edited
        if filter_img != "None":
            if filter_img == "Blur":
                filtered = edited.filter(BLUR)
            elif filter_img == "Detail":
                filtered = edited.filter(DETAIL)
            elif filter_img == "Emboss":
                filtered = edited.filter(EMBOSS)
            elif filter_img == "Smooth":
                filtered = edited.filter(SMOOTH)
        st.image(filtered)
