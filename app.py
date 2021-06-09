import streamlit as st
import pickle
import joblib
model = joblib.load('sentiment analysis')
st.title('Review-Analysis')
text = st.text_input('Enter the review message')
out = model.predict([text])
if st.button('Analysis'):
  st.title(out[0])
