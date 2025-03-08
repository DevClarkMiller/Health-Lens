import os
from pymongo import MongoClient
import pymongo
from dotenv import load_dotenv
load_dotenv()

client: MongoClient = None
db = None


def getDB():
    global client, db
    if client is None or db is None:
        client = pymongo.MongoClient(os.environ.get('MONGO_URL'))
        db = client["HealthLens"]

    return db

