import streamlit as st

st.title("Cloud Computing")

num = st.number_input('Pick a number', 0, 100)
st.write(num)
