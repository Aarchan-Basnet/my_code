# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000