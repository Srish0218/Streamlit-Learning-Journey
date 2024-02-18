import streamlit as st
import pandas as pd

st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4 , .st-emotion-cache-1wbqy5l.e17vllj40
{
     visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
# Streamlit app code
st.title("HI! I am Streamlit Web App")
st.subheader("HI! I am your SubHeader")
st.header("I am header")
st.text("HI I am text function")
st.markdown("**Hello** *World*")
# To run the app, you can use the command: streamlit run your_script.py

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
st.markdown("> blockquote")

st.markdown("---")
st.caption("HI i m caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

json = {"a": "1 , 2 ,3", "b": "4 , 5 , 6"}
st.json(json)

code = """
print("hello world")
def func():
    return 0;
"""
st.code(code, language="python")
st.markdown("---")
st.write("## H2")
st.metric(label="Wind speed", value="120 m/s", delta='-1.4m/s')

table = pd.DataFrame({"Column1": [1, 2, 3, 4, 5, 6, 7], "Column2": [11, 12, 13, 14, 15, 16, 17]})
st.table(table)

st.dataframe(table)

st.image('download.jpg', caption="Pycharm-Logo", width=100)
st.audio("sample.mp3")
st.video("sample.mp4")

st.markdown("---")


def change():
    print(st.session_state.checker)


state = st.checkbox("checkbox", value=True, on_change=change, key='checker')
if state:
    st.write("CHECKEDDDD")
else:
    pass

radio_btn = st.radio("Country?", options=("US", "UK", "India"))
st.write(radio_btn)


def btn_click():
    st.write("Clickeddd")


btn = st.button(":blue[Click ME]", on_click=btn_click())
btn2 = st.button("Click ME", on_click=btn_click())

select_car = st.selectbox("fav car?", options=("audi", "bmw", "maruti"))
st.write(select_car)

multi_select = st.multiselect("fav tech brand" , options = ("ms" , "apple" , "google" , "amazon"))
st.write(multi_select)

