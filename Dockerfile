FROM python:3.11

WORKDIR /code

COPY src/samdul03food/main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/DONGUK777/samdul03food.git@0.2.2

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
