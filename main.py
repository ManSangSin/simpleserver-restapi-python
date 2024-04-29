from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get ("/")
def read_root():
    return {"Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/tv_shows")
def get_shows():
    api_url = "https://api.tvmaze.com/shows"
    tv_shows_data = requests.get(api_url).json()
    specific_show = tv_shows_data[105]
    return specific_show