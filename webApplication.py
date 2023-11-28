import streamlit as st
import main

model = main.load_model()
text = st.text_input(label='Введите текст для перевода')
if text:
    translation = model(text)
    st.write(translation[0]['translation_text'])
