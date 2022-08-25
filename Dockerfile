FROM python:3.10.6

WORKDIR /api

COPY . /api

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "app:app", "--workers", "3", "-b", "0.0.0.0:5000"]
