from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

username = os.environ['USERNAME']
password = os.environ['PASSWORD']
host = os.environ['HOST']
port = os.environ['PORT']
database = os.environ['DATABASE']

#URL_DATABASE = 'postgresql://postgres:1234@postgres:5432/QuizApplication'
URL_DATABASE = f'postgresql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()