import dash_leaflet as dl
import pymongo
import os
from dotenv import load_dotenv
import dash_leaflet.express as dlx
from dash_extensions.javascript import assign
from datetime import datetime
import pymongo.database
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


def get_db(db_name: str):
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
            desc=item["description"],
            url=item["website"],
            rating=item["rating"],
            category=item["category"],
            lon=item["location"]["coordinates"][0],
            lat=item["location"]["coordinates"][1],
        )
        places.append(place)

    # geojson = dlx.dicts_to_geojson([{**c, **dict(popup="{0}/n{1}/n{2}".format(c["name"], c["rating"], c["desc"]))} for c in places])
    geojson = dlx.dicts_to_geojson([{**c, **dict(popup=c["name"])} for c in places])
    return geojson


def get_pin_icon():
    return assign(
        """function(feature, latlng){
        const flag = L.icon({iconUrl: `./assets/map-pin.png`, iconSize: [64, 48]});
        return L.marker(latlng, {icon: flag});
        }"""
    )

def get_one_listing(db, id):
    collection = db.listing_data
    listing = collection.find_one({"_id": id})
    places = [listing]
    geojson = dlx.dicts_to_geojson([{**c, **dict(popup=c["name"])} for c in places])
    return geojson

def create_listing(db, place_name: str, address: str, latitude: float, longitude: float, description: str, category: str, rating: float, website:str):
    current_date = datetime.now()

    item = {
        "place_name": place_name,
        "address": address,
        "latitude": latitude,
        "longitude": longitude,
        "description": description,
        "creation_date": current_date,
        "category": category,
        "rating": rating,
        "website": website,
        "location": {"type": "Point", "coordinates": [longitude, latitude]},
    }
    
    result = db.listing_data.insert_one(item)
    id = result.inserted_id
    return id
    

if __name__ == "__main__":
    t = datetime.now()
    print(t)