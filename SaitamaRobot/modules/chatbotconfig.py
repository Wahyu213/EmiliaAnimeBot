import os

from heroku3 import from_key
from pyrogram import Client

# My own ARQ API is Given. Don't fuck with it
API_ID = int(os.environ.get("API_ID", "6"))
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
ARQ_API_KEY = "MTXJXE-ELSWXE-UDRXJC-JCJQXN-ARQ" 
LANGUAGE = "en"
ARQ_API_BASE_URL = "https://thearq.tech"

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
