import streamlit as st

st.header("Hello World!")

num = st.number_input("Enter a num:", 1, 10)

if num:
    st.write(num)