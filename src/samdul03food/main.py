from typing import Union
import pickle
from fastapi import FastAPI

app = FastAPI()

# CSV 파일이 저장될 경로
csv_file_path = "/code/data/food.csv"

@app.get("/")
def read_root():
    return {"Hello": "n02"}

if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["food", "time"])  # 헤더 추가

@app.get("/food")
def food(name: str):
    # 현재 시간을 저장
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 음식 이름과 시간을 csv로 저장 _> /code/data/food.csv
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, current_time])  # 데이터 추가

    return {"food":name, "time": time}
