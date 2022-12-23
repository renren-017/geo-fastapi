import pymongo

from app.config import settings


DATABASE_URL = "mongodb://{}:{}@localhost:6000/{}}?authSource=admin".format(
    settings.MONGO_USER, settings.MONGO_PASS, settings.MONGO_DB
)
client = pymongo.mongo_client.MongoClient(DATABASE_URL)
print("CONNECTED TO MONGO")

db = client[settings.MONGO_DB]
Shop = db.shops