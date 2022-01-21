FROM python:latest
RUN apt-get update && apt-get upgrade -y
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./tapp ./tapp
CMD ['python3', './tapp/manage.py', 'runserver', '0.0.0.0:8000']