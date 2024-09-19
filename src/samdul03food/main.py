from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pytz
import uuid
import os
import csv

app = FastAPI()

origins = [
    "http://localhost:8899",
    "https://samdul03food-83d92.web.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "n03"}

@app.get("/food")
def food(name: str):
    # 시간을 구함
    # 음식 이름과 시간을 csv 로 저장 -> /code/data/food.csv
    # DB 저장
    print("==============" + name )

    from datetime import datetime
    import pytz
    timezone = pytz.timezone('Asia/Seoul')
    korea_time = datetime.now(timezone)
    formatted_time = korea_time.strftime('%Y-%m-%d %H:%M:%S')

    # DB
    import pymysql.cursors
    connection = pymysql.connect(host=os.getenv("DB_IP", "localhost"),
                             user='food',
                             password='1234',
                             database='fooddb',
                             port = int(os.getenv("DB_PORT", "13306")), 
                             cursorclass=pymysql.cursors.DictCursor)

    sql = "INSERT INTO foodhistory(`username`, `foodname`, `dt`) VALUES(%s,%s,%s)"
    
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, ('n03', name, formatted_time))
        connection.commit()

    # CSV
    file_path = os.getenv("FILE_PATH", f"{os.getenv('HOME')}/tmp/foodcsv/food.csv")
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    data = {"food": name, "time": formatted_time}
    with open(file_path, 'a', newline='') as f:
        csv.DictWriter(f, fieldnames=['food', 'time']).writerow(data)

    return {"food": name, "time": formatted_time}

