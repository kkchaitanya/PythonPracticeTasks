from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client.ticket_db
ticket_collection = db.tickets