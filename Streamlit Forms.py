import streamlit as st

st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4 , .st-emotion-cache-1wbqy5l.e17vllj40
{
     visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.title(" ***Streamlit Forms***")
st.markdown("---")
st.markdown("<h1 style = 'text-align: center;'> User Registeration </h1>" , unsafe_allow_html=True)
# form = st.form("Form 1")
# form.text_input("First Name")
# form.form_submit_button("Submit")
with st.form("Form 2" , clear_on_submit=True):
    col1 , col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    st.text_input("Email Address")
    pass1 , pass2 = st.columns(2)
    pass1.text_input("Password")
    pass2.text_input("Confirm Password")

    day , month , year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")

    s_state = st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please fill above fields!!!")
        else:
            st.success("Submitted")