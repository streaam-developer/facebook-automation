import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB settings
MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://sonukumarkrbbu60:lfkTvljnt25ehTt9@cluster0.2wrbftx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
DATABASE_NAME = 'facebook_automation'
COLLECTION_NAME = 'uploads'

# Facebook settings
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', 'EAFxZBUhsAQfEBQSs91FOLlZCvuFDtuFiF6qaOBzXJh1OOw23ba0GZCc7iZBwvSzKPehJt938dDgf1jjMOZCKuz3VqLhR7jkRKAN0kquYmOQDSVc4NdhZBINRJgGopDZA2F1OWdrrrYsxm8zZCc35ajn82bvt4uBfuOPKIXWAoj50V3bzClFoKuQVIe91Kli4wvX3')
FACEBOOK_PAGE_IDS = os.getenv('FACEBOOK_PAGE_IDS', '888810180973882,101568792628030').split(',')  # comma separated

# Instagram settings
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME', 'ankita_kum678')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD', 'ApqK*.J6HPbQ2B')

# Video settings
VIDEO_OUTPUT_DIR = 'data/videos'
EDITED_VIDEO_DIR = 'data/edited_videos'

# Logging
LOG_FILE = 'logs/automation.log'

# Web app settings
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'