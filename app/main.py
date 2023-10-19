from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pymongo import MongoClient
from decouple import config
from user_model import User
from user_controller import create_user, get_user


app = FastAPI()

# If MONGO_URL is not found in .env, it will default to mongodb://localhost:27017/test_database
MONGO_URL = config("MONGO_URL", default="mongodb://localhost:27017/test_database")

client = MongoClient(MONGO_URL)
db_name = "ws-auth"
db = client[db_name]

@app.get("/")
def read_root():
    item = db.test_collection.find_one()
    return {"Hello": "World", "MongoData": item}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/users/")
async def create_new_user(user: User):
    create_user(user)
    return {"msg": "User created successfully"}

@app.get("/users/{username}")
async def read_user(username: str):
    user = get_user(username)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.on_event("startup")
async def startup_event():
    admin_user = get_user("admin")
    if admin_user is None:
        create_user(User(username="admin", password="adminpassword", role="admin"))