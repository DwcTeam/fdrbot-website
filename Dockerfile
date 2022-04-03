FROM python:3.10-alpine

WORKDIR /

COPY . .

RUN pip install -r requirements.txt


CMD gunicorn --bind 0.0.0.0:80 app:app
