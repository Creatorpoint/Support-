import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_URL = os.getenv("MONGO_URL")

OWNER_ID = int(os.getenv("OWNER_ID"))
ADMINS = list(map(int, os.getenv("ADMINS").split(",")))

FORCE_CHANNEL = os.getenv("FORCE_CHANNEL")
