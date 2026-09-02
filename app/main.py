import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from app.routers.main_routes import mainrouter

load_dotenv()

app = FastAPI(title="Recommendation API", description="API for AI services", version="1.0.0")

app.include_router(mainrouter, prefix="/api/v1")

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
