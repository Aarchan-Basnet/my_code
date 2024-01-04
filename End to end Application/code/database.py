from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import insert
import json

def insert_into_sponsored_ads(db_url):
    print("Inserting sponsored ads into database ...")
    data = json.load(open('data/sponsored_ads.json'))

    engine = create_engine(db_url)
    meta = MetaData()

    sponsored_ads = Table(
        'sponsored_ads', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('item_name', String),
        Column('vendor', String),
        Column('discounted_price', String),
        Column('retail_price', String),
        Column('ratings', String),
        Column('total_reviews', String)
    )
    # meta.drop_all(bind=engine)
    meta.create_all(bind=engine)

    with engine.connect() as conn:
        conn.execute(
            insert(sponsored_ads),
            data,
        )
        conn.commit()
    print("Inserted Successfully.")

def insert_into_organic_ads(db_url):
    print("Inserting organic ads into databse ...")
    data = json.load(open('data/organic_ads.json'))

    engine = create_engine(db_url)
    meta = MetaData()

    organic_ads = Table(
        'organic_ads', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('title', String),
        Column('vendor', String),
        Column('landing_link', String)
    )
    # meta.drop_all(bind=engine)
    meta.create_all(bind=engine)

    with engine.connect() as conn:
        result = conn.execute(
            insert(organic_ads),
            data
        )
        conn.commit()
    print("Inserted successfully.")

db_url = 'postgresql://postgres:1234@postgres:5432/END2END'
def main():
    insert_into_sponsored_ads(db_url)
    insert_into_organic_ads(db_url)

if __name__ == "__main__":
    main()