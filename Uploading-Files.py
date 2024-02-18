import streamlit as st

st.title("Uploading Files...")
st.markdown("---")
images = st.file_uploader("Upload an image" , type = ["png" , "jpg"] , accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image , width = 100)