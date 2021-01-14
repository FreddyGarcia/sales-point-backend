FROM python:3.8

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_PORT 8000

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /app

RUN chmod 777 ./docker-setup.sh

RUN ./docker-setup.sh

CMD gunicorn app.wsgi --bind :$APP_PORT --worker-class gevent

EXPOSE 8000