from user_model import User
from db_util import get_collection
import hashlib

user_collection = get_collection("users")

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(user: User):
    user.password = hash_password(user.password)
    user_collection.insert_one(user.dict())

def get_user(username: str):
    user_data = user_collection.find_one({"username": username})
    if user_data:
        return User(**user_data)
