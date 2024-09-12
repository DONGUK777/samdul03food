from typing import Union
import pickle
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "n02"}

@app.get("/food")
def food(name: str):
    # 시간을 구함
    # 음식 이름과 시간을 csv로 저장 _> /code/data/food.csv
    return {"food":name, "time": "2024-09-15 11:12:13"}
