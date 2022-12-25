from pymongo import MongoClient

from app.config import settings

mongo_client = MongoClient(host=settings.MONGO_HOST,
                           port=int(settings.MONGO_PORT),
                           username=settings.MONGO_INITDB_USERNAME,
                           password=settings.MONGO_INITDB_PASSWORD)

db = mongo_client[settings.MONGO_INITDB_DATABASE]

shop_collection = db["shops"]


def shop_helper(shop) -> dict:
    return {
        "id": str(shop["_id"]),
        "name": shop["name"],
        "lat": shop["lat"],
        "lon": shop["lon"],
        "address": shop["address"],
        "city": shop["city"],
    }