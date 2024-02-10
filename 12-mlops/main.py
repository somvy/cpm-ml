from typing import Union

from fastapi import FastAPI
from model import generate_text

app = FastAPI()





@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/generate_text")
def read_item(prompt: str, max_len: int = 100):
    return generate_text(prompt, max_len)
