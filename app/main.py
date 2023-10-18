from fastapi import FastAPI
from pymongo import MongoClient
from decouple import config

app = FastAPI()

# If MONGO_URL is not found in .env, it will default to mongodb://localhost:27017/test_database
MONGO_URL = config("MONGO_URL", default="mongodb://localhost:27017/test_database")

client = MongoClient(MONGO_URL)
db_name = MONGO_URL.split('/')[-1]  # Extract the database name from the URL
db = client[db_name]

@app.get("/")
def read_root():
    item = db.test_collection.find_one()
    return {"Hello": "World", "MongoData": item}