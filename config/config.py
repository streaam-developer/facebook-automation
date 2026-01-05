import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB settings
MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://sonukumarkrbbu60:lfkTvljnt25ehTt9@cluster0.2wrbftx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
DATABASE_NAME = 'facebook_automation'
COLLECTION_NAME = 'uploads'

# Facebook settings
FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', 'EAFxZBUhsAQfEBQUO9BfHTM48Sa6ZB321dCeuDSYoWpR8RpQytBZA7ZAwiJwy8Cq9ZCFkEl85ifmvroAZAs6aFp3SIEb4h6zTZBQkzqXWDAbaobMV5vj4gKAizLWR31IrBht3HwddXOzUHiuCpWIIoTkpnSZCZBnyEXSg1OhsEvFX6bZAQlsxZANZBzPmwFEixmkw2n4N')
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