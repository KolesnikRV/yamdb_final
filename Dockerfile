FROM python:3.8.5

LABEL author='BrainTake@yandex.ru' version=1.1

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000