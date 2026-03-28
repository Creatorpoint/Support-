from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)
db = client.support_bot

users = db.users
banned = db.banned

async def add_user(user_id):
    if not await users.find_one({"_id": user_id}):
        await users.insert_one({"_id": user_id})

async def get_users():
    return [u["_id"] async for u in users.find()]

async def ban_user(user_id):
    await banned.insert_one({"_id": user_id})

async def is_banned(user_id):
    return await banned.find_one({"_id": user_id})
