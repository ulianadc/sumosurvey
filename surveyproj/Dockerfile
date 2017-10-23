FROM python:3.6

MAINTAINER David Uliana <ulianadc@gmail.com>

RUN apt-get update -y
RUN apt-get install -y libmysqlclient-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /sumo/requirements.txt
RUN pip install --requirement /sumo/requirements.txt
