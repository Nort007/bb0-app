FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Подгрузить в entrypoint скрипты

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apt-get update && apt-get upgrade -y

RUN mkdir /tapp
COPY /tapp /tapp
WORKDIR /tapp

COPY ./tapp ./tapp

COPY ./scripts/ ./scripts/

RUN chmod +x ./scripts/*.sh

RUN mkdir -p /vol/web/static
RUN chmod -R 755 /vol/web

ENTRYPOINT ["sh", "./scripts/entrypoint.sh"]
