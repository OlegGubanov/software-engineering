from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_model():
    return pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")


model = load_model()
text = st.text_input(label='Введите текст для перевода')
if text:
    translation = model(text)
    st.write(translation[0]['translation_text'])
