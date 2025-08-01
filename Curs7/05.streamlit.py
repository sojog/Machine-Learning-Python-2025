# pip install streamlit
import streamlit as st

x = st.slider("Select a value")
st.write(x, "squared is", x * x)


nume = st.chat_input("Care este numele tau??")
print(nume)