from fastapi import FastAPI
from app.api.v1 import user
from app.core.config import settings
from app.db import init_db, get_database

app = FastAPI()

app.include_router(user.router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    await init_db()

@app.on_event("shutdown")
async def shutdown():
    from tortoise import Tortoise
    await Tortoise.close_connections()

# If you need to use the database connection in a route:
@app.get("/")
async def root():
    db = await get_database()
    # Use db for database operations
    return {"message": "Hello World"}