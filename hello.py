import streamlit as st

st.title("Streamlit Web-App!")

name = st.text_input("Enter your name:")
msg = "Hello {}!".format(name)

number = st.number_input("Enter a no:", 1, 5)

if name:
    st.write(msg)