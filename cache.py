import time
import streamlit as st


@st.cache(suppress_st_warning=True)
def printer():
    st.write("Running...")
    time.sleep(3)
    return "Message"


st.write(printer())
