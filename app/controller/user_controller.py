from app.db.mongodb import db
from app.models.user import User
from app.models.interaction import Interaction

def all_users():
    users = db.users.find()
    return [User(**user) for user in users]

def user_by_id(user_id: str):
    user = db.users.find_one({"_id": user_id})
    if user:
        return User(**user)
    return None

def next_products(user_id: str, limit: int = 2):
    # Placeholder implementation - replace with actual product recommendation logic
    interactions = db.interactions.find({"user_id": user_id}).sort("timestamp", -1).limit(limit)
    return [Interaction(**interaction) for interaction in interactions]