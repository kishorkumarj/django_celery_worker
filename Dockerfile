FROM python:3.10.6-alpine

RUN mkdir /app

WORKDIR /app
RUN pip install --upgrade pip
COPY . /app/
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "app_server.wsgi", "--workers=4", "--bind=0.0.0.0:8000"]
