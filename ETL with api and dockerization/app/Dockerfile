FROM python:3.9-alpine
RUN pip install fastapi uvicorn psycopg2-binary sqlalchemy
COPY . /
EXPOSE 8000
CMD uvicorn main:app --host 0.0.0.0 --port 8000