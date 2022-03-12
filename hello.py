import streamlit as st

st.title("Streamlit Web-App!")

name = st.text_input("Enter your name:")
msg = "Hello {}!".format(name)

if name:
    st.write(msg)