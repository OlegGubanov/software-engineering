
# Russian-to-English Translator

API и веб-интерфейс для перевода текста с русского языка на английский.

# Команда

- Майоров Егор Сергеевич (РИМ-130906)
- Губанов Олег Юрьевич (РИМ-130906)

# Модель

**[Helsinki-NLP/opus-mt-ru-en](https://huggingface.co/Helsinki-NLP/opus-mt-ru-en)**

Модель для автоматического перевода текста с исходного языка на целевой.

- Разработана Language Technology Research Group at the University of Helsinki
- Тип модели: Transformer-Align
- Языки:
  - Исходный: русский
  - Целевой: английский
- Лицензия: CC-BY-4.0
- Дополнительная информация:
  - [Репозиторий на GitHub](https://github.com/Helsinki-NLP/OPUS-MT-train)

# Использование

## Установка
```
# Скачиваем проект и устанавливаем необходимые библиотеки
git clone https://github.com/OlegGubanov/software-engineering.git
pip install -r requirements.txt
```

## API
```
# Запускаем FastAPI
uvicorn fastApi:app

# Отправляем POST-запрос
curl -X POST \
    http://127.0.0.1:8000/translate \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"text": "Привет, мир!"}'
```

## Web

```
# Запускаем Streamlit-приложение
streamlit run webApplication.py

# Вводим в браузере текст для перевода
```
