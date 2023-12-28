FROM python:3.9-alpine
RUN pip install selenium lxml psycopg2-binary sqlalchemy
COPY . /
EXPOSE 8001
CMD python3 main.py