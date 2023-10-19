from pymongo import MongoClient
from decouple import config

def get_db():
    MONGO_URL = config("MONGO_URL", default="mongodb://localhost:27017/test_database")

    client = MongoClient(MONGO_URL)
    db_name = "ws-auth"
    db = client[db_name]
    return db