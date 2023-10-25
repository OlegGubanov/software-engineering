from transformers import pipeline

translator_ru_to_en = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")
word = translator_ru_to_en(input())[0]['translation_text']
print(word)