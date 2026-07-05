import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8629866531:AAFvBUiVxmDKEVGVifa2i9UR3QBMqHmtU2Q")
SMSBOWER_API_KEY = os.getenv("5VKQe0tU9J7JvccBr0fCB3PbVHGiq7by")
ADMIN_ID = int(os.getenv("6715426106", "0"))