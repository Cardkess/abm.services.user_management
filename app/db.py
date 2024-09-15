from tortoise import Tortoise, fields, Model, connections
from app.core.config import settings

TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.user"],
            "default_connection": "default",
        },
    },
}

async def init_db():
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()

# Instead, use this function to get the database connection when needed:
async def get_database():
    return connections.get("default")