import streamlit as st

def printer(name): #call back
    print("Name:" , name)
input_val = st.text_input("Enter your name:")
s_btn = st.button("Submit")

if s_btn:
    opt = st.checkbox("Want to display your name?" , on_change= printer , args=(input_val , ))
    # if opt:
    #     print(input_val) # does not print the name so we neeed call back
