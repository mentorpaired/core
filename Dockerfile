FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc libpq-dev python-dev && \
    apt-get clean

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /mentorpaired_core
WORKDIR /mentorpaired_core
COPY ./requirements.txt /mentorpaired_core/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /mentorpaired_core/

ENTRYPOINT ["/mentorpaired_core/entrypoint.sh"]
