# pip install streamlit
import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# MESSAGES_KEY = "messages"

with open("model.pkl", "rb") as freader:
    model:LinearRegression = pickle.load(freader)

metri_patrati = st.chat_input("Cati metri patrati are apartamentul tau??")
print(metri_patrati)


print("st.session_state:", st.session_state)

# if not st.session_state.get(MESSAGES_KEY):
#     st.session_state[MESSAGES_KEY] = []

print("st.session_state:", st.session_state)

with st.chat_message("human") as chat_message:
    st.write(metri_patrati)
    try:
        metri_patrati = float(metri_patrati)
        pret = model.predict([[metri_patrati]])
        with st.chat_message("ai") as chat_message:
            pret = int(pret[0])
            st.write(f"Ar trebui sa il vinzi cu {pret} 000 Euro")
    except:
        with st.chat_message("ai") as chat_message:
            st.write("Nu e corect")
    

    