from fastapi import APIRouter
from app.controller.user_controller import all_users, user_by_id, next_products

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    return all_users()

@router.get("/{user_id}")
def get_user(user_id: str):
    user = user_by_id(user_id)
    if user:
        return user
    return {"message": "User not found"}

@router.get("/{user_id}/products")
def get_next_products(user_id: str, limit: int = 2):
    return next_products(user_id, limit)