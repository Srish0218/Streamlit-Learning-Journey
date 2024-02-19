import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("***Sidebar & Graphs In Streamlit***")
st.markdown("---")

# Elements in the sidebar
graph = st.sidebar.radio("Select Any Graph", options=("Line", "Bar", "Histogram"))

x = np.linspace(0, 10, 100)

if graph == "Line":
    st.markdown("<h1 style='text-align:center;'> Line Chart </h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle')
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.cos(x), label='cos(x)')
    plt.legend()
    st.pyplot(fig)
elif graph == "Bar":
    st.markdown("<h1 style='text-align:center;'> Bar Chart </h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle')
    data = np.random.randn(1000)
    plt.bar(x, x * 10)
    st.write(fig)
elif graph == "Histogram":
    st.markdown("<h1 style='text-align:center;'> Histogram </h1>", unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle')
    data = np.random.randn(1000)
    plt.hist(data, bins=30, color='skyblue', edgecolor='black')
    st.pyplot(fig)
