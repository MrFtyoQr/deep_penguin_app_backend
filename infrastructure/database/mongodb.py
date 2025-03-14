import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "your_default_mongodb_uri_here")
client = MongoClient(MONGO_URI)
db = client.get_database("study_guide")
study_guides_collection = db.get_collection("guides")
