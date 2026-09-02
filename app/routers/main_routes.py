from fastapi import APIRouter

from app.routers import user_routes, products_routes

mainrouter = APIRouter()

mainrouter.include_router(user_routes.router)
mainrouter.include_router(products_routes.router)

@mainrouter.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}