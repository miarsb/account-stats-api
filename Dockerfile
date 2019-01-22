FROM python:3.7

RUN apt-get update
RUN apt-get -y install nginx

RUN mkdir /api
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY key.txt /api
copy api.py /api
copy api_helpers.py /api
COPY __init__.py /api

COPY scores /api/scores


WORKDIR /api


CMD ./startup.sh