import dash_leaflet as dl
import pymongo
import os
from dotenv import load_dotenv
import dash_leaflet.express as dlx
from dash_extensions.javascript import assign
from datetime import datetime
from pytz import timezone

load_dotenv()

def get_timestamp():
    utc = timezone("UTC")
    eastern = timezone("America/Montreal")
    date = datetime.now(tz=eastern)
    return date
    

def create_db_client():
    client = pymongo.MongoClient(
        "mongodb+srv://{0}:{1}@cluster0.c3trx.mongodb.net/?retryWrites=true&w=majority&appName={2}".format(
            os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_APPNAME")
        )
    )
    return client


def get_db(db_name):
    client = create_db_client()
    db = client[db_name]
    return db


def get_db_data(db, collection_name):
    collection = db[collection_name]
    data = collection.find()
    return data


def get_geo_data(data):
    places = []
    for item in data:
        place = dict(
            name=item["place_name"],
            lon=item["location"]["coordinates"][0],
            lat=item["location"]["coordinates"][1],
        )
        places.append(place)

    geojson = dlx.dicts_to_geojson([{**c, **dict(popup=c["name"])} for c in places])
    return geojson


def get_pin_icon():
    return assign(
        """function(feature, latlng){
        const flag = L.icon({iconUrl: `./assets/map-pin.png`, iconSize: [64, 48]});
        return L.marker(latlng, {icon: flag});
        }"""
    )


def create_listing(db, place_name: str, address: str, latitude: float, longitude: float, description: str, category: str, rating: float, website:str):
    timestamp = get_timestamp()
    item = {
        "place_name": place_name,
        "address": address,
        "latitude": latitude,
        "longitude": longitude,
        "description": description,
        "creation_date": timestamp,
        "category": category,
        "rating": rating,
        "website": website,
        "location": {"type": "Point", "coordinates": [longitude, latitude]},
    }
    result = db.listing_data.insert_one(item)
    id = result.inserted_id
    return id
    

# if __name__ == "__main__":
#     t = get_timestamp()
#     print(t)