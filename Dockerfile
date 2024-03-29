FROM python:3.6
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /code:$PYTHONPATH

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code

RUN pip install -r requirements.txt

COPY . /code/
