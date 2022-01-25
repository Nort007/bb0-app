FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apt-get update && apt-get upgrade -y

RUN mkdir /tapp
COPY /tapp /tapp
WORKDIR /tapp

COPY ./tapp ./tapp

RUN mkdir -p /vol/web/static
RUN chmod -R 755 /vol/web

CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
