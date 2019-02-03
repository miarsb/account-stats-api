FROM python:3.7

RUN mkdir /api
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY 39310-9864214f13c8.json /api
copy api.py /api
copy api_helpers.py /api
COPY __init__.py /api

COPY scores /api/scores

WORKDIR /api


CMD gunicorn api:app -b :8080 
