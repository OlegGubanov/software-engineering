import main
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    text: str


model = main.load_model()
app = FastAPI()


@app.post('/translate')
async def translate(item: Item):
    return model(item.text)[0]['translation_text']
