from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os
from os import path

conn = MongoClient(os.getenv("MONGO_CREDENTIALS"))
# print(conn)
# print("XXX", os.getenv("MONGO_CREDENTIALS"))
PORT_DB = os.getenv("PORT_DB")

db = conn[PORT_DB]