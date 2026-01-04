from pymongo import MongoClient
from config.config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME
import datetime

class Database:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def insert_upload(self, reel_url, video_path, edited_path, facebook_results):
        doc = {
            'reel_url': reel_url,
            'video_path': video_path,
            'edited_path': edited_path,
            'facebook_results': facebook_results,
            'timestamp': datetime.datetime.utcnow(),
            'status': 'completed' if all(r['status'] == 'success' for r in facebook_results.values()) else 'partial'
        }
        return self.collection.insert_one(doc)

    def get_uploads(self, limit=10):
        return list(self.collection.find().sort('timestamp', -1).limit(limit))

if __name__ == "__main__":
    db = Database()
    # Example insert
    db.insert_upload("https://instagram.com/reel/123", "path", "edited_path", {"page1": {"status": "success"}})