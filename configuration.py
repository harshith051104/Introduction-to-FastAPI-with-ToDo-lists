
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db=client.todo_db
collection = db["todo_data"]