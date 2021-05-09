FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip -U install pip

RUN pip install -r requirements.txt