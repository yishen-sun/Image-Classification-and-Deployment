FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./inference.py /app/inference.py
COPY ./flask_api /app/flask_api
COPY ./src /app/src

CMD python3 /app/inference.py