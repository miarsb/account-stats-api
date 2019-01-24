FROM python:3.7

RUN mkdir /api
COPY requirements.txt .
RUN pip install -r requirements.txt

copy api.py /api
copy api_helpers.py /api
COPY __init__.py /api

COPY scores /api/scores


WORKDIR /api


CMD gunicorn api:app -b :8080 
