import time as ts
from datetime import time
import streamlit as st

st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4 , .st-emotion-cache-1wbqy5l.e17vllj40
{
     visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

val = st.slider("This is a Slider", min_value=50, max_value=150, value=70)
st.write(val)

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

st.markdown("---")

val2 = st.text_input("Course title: ", max_chars=60)
st.write(val2)
textarea = st.text_area("Description")
st.write(textarea)

st.markdown("---")

date = st.date_input("DOB")
st.write(date)

st.markdown("---")


# Timer App With Progress Bar
st.title("Timer App With Progress Bar...")
def converter(value):
    m , s , mm = value.split(":")
    t_s = int(m) * 60 + int(s) + int(mm)/1000
    return t_s

timer = st.time_input("Set Timer", value=time(0, 0, 0))
st.write(timer)
if str(timer) == "00:00:00":
    st.write("Please set timer...")
else:
    sec = converter(str(timer))
    bar = st.progress(0)
    percent = sec / 100
    progress_status = st.empty()
    for i in range(100):
        bar.progress(i + 1)
        progress_status.write(str(i) + " %")
        ts.sleep(percent)