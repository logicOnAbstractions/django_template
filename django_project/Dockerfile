FROM python:3.9

WORKDIR /usr/src/django_project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# psycog2 dependancies
RUN apt-get update \
    && apt-get install -y postgresql gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .