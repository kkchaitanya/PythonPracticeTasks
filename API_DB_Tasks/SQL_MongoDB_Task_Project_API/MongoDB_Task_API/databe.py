from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client.Project_Tasks
tasks = db.tasks
project =db.projects