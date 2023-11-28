from transformers import pipeline


def load_model():
    return pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")

