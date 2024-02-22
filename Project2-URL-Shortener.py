import streamlit as st
import pyshorteners as pyst
import pyperclip

shortener = pyst.Shortener()

st.markdown("<h1 style='text-align:center;'>URL Shortener</h1>", unsafe_allow_html=True)
st.markdown("---")

form = st.form("URL-Shortener")
url = form.text_input("Enter URL")
s_btn = form.form_submit_button("Submit")

def copyurl(shorted_url):
    pyperclip.copy(shorted_url)

if s_btn:
    shorted_url = shortener.tinyurl.short(url)
    st.markdown("<h3>SHORTENED URL</h3>", unsafe_allow_html=True)
    st.markdown(f'<h6 style="text-align:center;">{shorted_url}</h6>', unsafe_allow_html=True)
    st.button("Copy", on_click=copyurl, args=(shorted_url,))
