import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB settings
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DATABASE_NAME = 'facebook_automation'
COLLECTION_NAME = 'uploads'

# Facebook settings
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN')
FACEBOOK_PAGE_IDS = os.getenv('FACEBOOK_PAGE_IDS', '').split(',')  # comma separated

# Instagram settings
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

# Video settings
VIDEO_OUTPUT_DIR = 'data/videos'
EDITED_VIDEO_DIR = 'data/edited_videos'

# Logging
LOG_FILE = 'logs/automation.log'

# Web app settings
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'