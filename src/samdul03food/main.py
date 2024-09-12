from typing import Union
import pandas as pd
from datetime import datetime
from fastapi import FastAPI
import os

app = FastAPI()

# CSV 파일이 저장될 경로
csv_file_path = "/code/data/food.csv"
csv_dir_path = os.path.dirname(csv_file_path)

# 디렉터리가 없으면 생성
if not os.path.exists(csv_dir_path):
    os.makedirs(csv_dir_path)

# 서버가 시작될 때 헤더가 없는 파일일 경우, 헤더 추가
if not os.path.exists(csv_file_path):
    df = pd.DataFrame(columns=["food", "time"])
    df.to_csv(csv_file_path, index=False, encoding='utf-8')  # 헤더와 빈 데이터로 파일 생성

@app.get("/")
def read_root():
    return {"Hello": "n02"}

@app.get("/food")
def food(name: str):
    # 현재 시간을 저장
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 음식 이름과 시간을 DataFrame으로 변환
    df = pd.DataFrame([[name, current_time]], columns=["food", "time"])

    # DataFrame을 CSV 파일에 추가
    try:
        df.to_csv(csv_file_path, mode='a', header=False, index=False, encoding='utf-8')
    except Exception as e:
        print(f"Error writing to CSV: {e}")

    return {"food": name, "time": current_time}

