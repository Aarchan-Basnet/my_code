from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.automap import automap_base
db_url = "postgresql://postgres:1234@postgres:5432/END2END"

engine = create_engine(db_url)

Base = automap_base()
Base.prepare(autoload_with=engine)
sponsored_ads = Base.classes.sponsored_ads
organic_ads = Base.classes.organic_ads
session = Session(engine)

app = FastAPI()

@app.get("/")
def read():
    return {"message": "Hello World"}

@app.get("/sponsored_ads/all")
async def read_table():
    q_list = session.query(sponsored_ads).all()
    data_list = []
    for u1 in q_list:
        data = {
            "id": u1.id,
            "item_name": u1.item_name,
            "vendor": u1.vendor,
            "discounted_price": u1.discounted_price,
            "retail_price": u1.retail_price,
            "ratings": u1.ratings,
            "total_reviews": u1.total_reviews
        }
        data_list.append(data)
    return data_list

@app.get("/sponsored_ads/{ads_id}")
async def read_table(ads_id: int):
    u1 = session.query(sponsored_ads).filter(sponsored_ads.id == ads_id).first()
    data = {
        "id": u1.id,
        "item_name": u1.item_name,
        "vendor": u1.vendor,
        "discounted_price": u1.discounted_price,
        "retail_price": u1.retail_price,
        "ratings": u1.ratings,
        "total_reviews": u1.total_reviews
    }
    return data

@app.get("/organic_ads/all")
async def read_table():
    q_list = session.query(organic_ads).all()
    data_list = []
    for u1 in q_list:
        data = {
            "id": u1.id,
            "title": u1.title,
            "vendor": u1.vendor,
            "landing_link": u1.landing_link
        }
        data_list.append(data)
    return data_list

@app.get("/organic_ads/{ads_id}")
async def read_table(ads_id: int):
    u1 = session.query(organic_ads).filter(organic_ads.id == ads_id).first()
    data = {
        "id": u1.id,
        "title": u1.title,
        "vendor": u1.vendor,
        "landing_link": u1.landing_link
    }
    return data
